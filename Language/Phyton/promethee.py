import pandas as pd
import numpy as np

# Data input
# Create a dictionary containing the data for alternatives (students) and their scores for each criterion (C1 to C5).
data = {
    "Mahasiswa": ["Apart Variz", "Apart Tio", "Apart Diana", "Apart Vidi", "Apart Fajar"],
    "C1": [2, 2, 2, 7, 3],  # Scores for criterion C1
    "C2": [4, 1, 3, 2, 3],  # Scores for criterion C2
    "C3": [3, 2, 2, 4, 4],  # Scores for criterion C3
    "C4": [4, 2, 3, 3, 2],  # Scores for criterion C4
    "C5": [1, 3, 2, 1, 3],  # Scores for criterion C5
}

# Convert the data dictionary into a Pandas DataFrame for easier manipulation.
df = pd.DataFrame(data)

# Set the "Mahasiswa" column as the index to represent alternatives (students).
df.set_index("Mahasiswa", inplace=True)

# Informasi kriteria
# Define the criteria information, including:
# - Type: Whether the criterion is a "benefit" (higher is better) or "cost" (lower is better).
# - Weight: The importance of the criterion in the decision-making process.
# - Preference type: The type of preference function to use for pairwise comparisons.
# - Thresholds (q and p): Used for specific preference types.
kriteria_info = {
    "C1": {"type": "benefit", "weight": 0.3, "pref_type": "I"},  # Usual preference
    "C2": {"type": "cost", "weight": 0.2, "pref_type": "V", "q": 0.5, "p": 2},  # Linear with thresholds
    "C3": {"type": "benefit", "weight": 0.2, "pref_type": "II", "q": 1},  # U-shape preference
    "C4": {"type": "cost", "weight": 0.2, "pref_type": "III", "p": 2},  # V-shape preference
    "C5": {"type": "benefit", "weight": 0.1, "pref_type": "I"},  # Usual preference
}

# Fungsi preferensi
# Define the preference function to calculate the degree of preference between two alternatives.
def preference_function(d, tipe, q=0, p=0):
    # Usual preference: Returns 1 if the difference is positive, otherwise 0.
    if tipe == "I":  
        return 0 if d <= 0 else 1
    # U-shape preference: Returns 1 if the difference exceeds the threshold q, otherwise 0.
    elif tipe == "II":  
        return 0 if d <= q else 1
    # V-shape preference: Returns a linear value between 0 and 1 based on the threshold p.
    elif tipe == "III":  
        return d / p if d < p else 1
    # Linear with indifference and preference thresholds: Gradually increases from 0 to 1 between q and p.
    elif tipe == "V":  
        if d <= q:
            return 0
        elif d < p:
            return (d - q) / (p - q)
        else:
            return 1
    # Default case: Returns 0 if no valid preference type is provided.
    else:
        return 0

# Langkah 1 & 2: Hitung nilai preferensi antar pasangan alternatif
# Step 1 & 2: Calculate the preference values between all pairs of alternatives.
alternatives = df.index.tolist()  # List of alternatives (students).
n = len(alternatives)  # Number of alternatives.

# Initialize a matrix to store the aggregated preference values for each pair of alternatives.
pi_matrix = pd.DataFrame(0, index=alternatives, columns=alternatives, dtype=float)

# Loop through all pairs of alternatives (i, j).
for i in range(n):
    for j in range(n):
        if i == j:
            continue  # Skip comparisons of an alternative with itself.
        pi_sum = 0  # Initialize the sum of weighted preference values for this pair.
        for crit in df.columns:  # Loop through all criteria.
            val_i = df.iloc[i][crit]  # Value of alternative i for the current criterion.
            val_j = df.iloc[j][crit]  # Value of alternative j for the current criterion.
            info = kriteria_info[crit]  # Get the criterion's information.
            # Calculate the difference based on whether the criterion is a benefit or cost.
            diff = val_i - val_j if info["type"] == "benefit" else val_j - val_i
            # Calculate the preference value using the preference function.
            pref_val = preference_function(diff, info["pref_type"], info.get("q", 0), info.get("p", 0))
            # Multiply the preference value by the criterion's weight and add it to the sum.
            pi_sum += info["weight"] * pref_val
        # Store the aggregated preference value in the matrix.
        pi_matrix.iloc[i, j] = pi_sum

# Langkah 3: Hitung leaving flow, entering flow, dan net flow
# Step 3: Calculate the leaving flow, entering flow, and net flow for each alternative.
phi_plus = pi_matrix.sum(axis=1) / (n - 1)  # Leaving flow: Average preference given by an alternative.
phi_minus = pi_matrix.sum(axis=0) / (n - 1)  # Entering flow: Average preference received by an alternative.
phi_net = phi_plus - phi_minus  # Net flow: Difference between leaving and entering flows.

# Gabungkan hasil
# Combine the results into a DataFrame for easier interpretation and sorting.
result_df = pd.DataFrame({
    "Leaving Flow (phi+)": phi_plus,  # Add leaving flow to the result.
    "Entering Flow (phi-)": phi_minus,  # Add entering flow to the result.
    "Net Flow (phi)": phi_net  # Add net flow to the result.
}).sort_values("Net Flow (phi)", ascending=False)  # Sort alternatives by net flow in descending order.

# Print the final result, showing the ranking of alternatives based on their net flow.
print(result_df)