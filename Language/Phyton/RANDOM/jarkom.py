import matplotlib.pyplot as plt
import numpy as np

# Bit input setelah ditambah absen ke-29 (11101)
bits = '10101001100011100101100011101'
bit_array = [int(b) for b in bits]

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
titles = ["NRZ-L", "NRZ-I", "AMI", "Pseudoternary", "Manchester", "Differential Manchester"]

def plot_signal(ax, title, levels, color, bit_len=1):
    signal = []
    for level in levels:
        signal += [level] * 100
    signal.append(signal[-1])
    time = np.linspace(0, len(levels), len(signal))
    ax.plot(time, signal, drawstyle='steps-post', color=color, linewidth=2.5)
    ax.set_title(title, fontsize=11, fontweight='bold')
    ax.set_ylim(-2, 2)
    ax.set_xlim(0, len(levels))
    ax.set_ylabel('Level', fontsize=9)
    ax.grid(True, linestyle=':', alpha=0.7)
    ax.set_xticks(np.arange(0, len(levels)+1, 1))
    ax.set_yticks([-1, 0, 1])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

def nrzl(bits):
    return [1 if b == 1 else -1 for b in bits]

def nrzi(bits):
    signal = []
    last = 1
    for b in bits:
        if b == 1:
            last *= -1
        signal.append(last)
    return signal

def ami(bits):
    signal = []
    level = 1
    for b in bits:
        if b == 0:
            signal.append(0)
        else:
            signal.append(level)
            level *= -1
    return signal

def pseudoternary(bits):
    signal = []
    level = 1
    for b in bits:
        if b == 1:
            signal.append(0)
        else:
            signal.append(level)
            level *= -1
    return signal

def manchester(bits):
    signal = []
    for b in bits:
        if b == 1:
            signal += [1, -1]
        else:
            signal += [-1, 1]
    return signal

def diff_manchester(bits):
    signal = []
    last = -1
    for b in bits:
        if b == 0:
            last *= -1
            signal += [last, -last]
        else:
            signal += [last, -last]
    return signal

plt.style.use('seaborn-v0_8-darkgrid')
fig, axs = plt.subplots(6, 1, figsize=(15, 11), sharex=True)
fig.suptitle('Line Coding Schemes', fontsize=16, fontweight='bold', color='#333333')

plot_signal(axs[0], titles[0], nrzl(bit_array), colors[0])
plot_signal(axs[1], titles[1], nrzi(bit_array), colors[1])
plot_signal(axs[2], titles[2], ami(bit_array), colors[2])
plot_signal(axs[3], titles[3], pseudoternary(bit_array), colors[3])

# Manchester
manchester_sig = manchester(bit_array)
signal = []
for level in manchester_sig:
    signal += [level] * 50
signal.append(signal[-1])
time = np.linspace(0, len(bit_array), len(signal))
axs[4].plot(time, signal, drawstyle='steps-post', color=colors[4], linewidth=2.5)
axs[4].set_title(titles[4], fontsize=11, fontweight='bold')
axs[4].set_ylim(-2, 2)
axs[4].set_xlim(0, len(bit_array))
axs[4].set_ylabel('Level', fontsize=9)
axs[4].grid(True, linestyle=':', alpha=0.7)
axs[4].set_yticks([-1, 0, 1])
axs[4].spines['top'].set_visible(False)
axs[4].spines['right'].set_visible(False)

# Differential Manchester
diff_manchester_sig = diff_manchester(bit_array)
signal = []
for level in diff_manchester_sig:
    signal += [level] * 50
signal.append(signal[-1])
time = np.linspace(0, len(bit_array), len(signal))
axs[5].plot(time, signal, drawstyle='steps-post', color=colors[5], linewidth=2.5)
axs[5].set_title(titles[5], fontsize=11, fontweight='bold')
axs[5].set_ylim(-2, 2)
axs[5].set_xlim(0, len(bit_array))
axs[5].set_ylabel('Level', fontsize=9)
axs[5].grid(True, linestyle=':', alpha=0.7)
axs[5].set_yticks([-1, 0, 1])
axs[5].spines['top'].set_visible(False)
axs[5].spines['right'].set_visible(False)

axs[-1].set_xlabel('Bit Index', fontsize=11, fontweight='bold')

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()