# 1. Import Library
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
import joblib

# 2. Load Dataset
df = pd.read_csv("training_dataset.csv")

# 3. Encoding fitur kategorikal
categorical_cols = df.select_dtypes(include='object').columns
label_encoders = {}
for col in categorical_cols:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# 4. Menentukan fitur & target
X = df.drop(columns=["customer_number", "berlangganan_deposito"])
y = df["berlangganan_deposito"]

# 5. Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 6. Melatih Model
model = RandomForestClassifier(class_weight="balanced", random_state=42)
model.fit(X_train, y_train)

# 7. Evaluasi AUC
y_pred_prob = model.predict_proba(X_test)[:, 1]
auc = roc_auc_score(y_test, y_pred_prob)
print(f"AUC: {auc:.4f}")

# 8. Simpan prediksi dalam format CSV
df_submission = pd.DataFrame({
    "customer_number": df.loc[X_test.index, "customer_number"].astype(int),
    "berlangganan_deposito": y_pred_prob
})
df_submission["berlangganan_deposito"] = df_submission["berlangganan_deposito"].round(10)
df_submission = df_submission.drop_duplicates(subset="customer_number")
df_submission = df_submission.dropna()
df_submission.to_csv("sample_data/submission_example.csv", index=False)
print("File submission_example.csv berhasil disimpan dengan format rapi.")

# 9. Merapikan CSV
data = pd.read_csv("sample_data/submission_example.csv")
data['berlangganan_deposito'] = data['berlangganan_deposito'].round(3)
data.to_excel("submission_final.xlsx", index=False)
