import matplotlib.pyplot as plt
import numpy as np

# Set up the figure
plt.figure(figsize=(15, 4), dpi=100)
plt.style.use('seaborn-whitegrid')

# Sample data with fewer points
samples = 100  # Reduced from 1000 to make lines simpler
time_acc = np.linspace(0, 70000, samples)
time_others = np.linspace(0, 400000, samples)

# 1. Acceleration Data (Simplified)
plt.subplot(1, 3, 1)
plt.plot(time_acc, -800 * np.sin(time_acc/5000), 'r-', linewidth=1.5, label='Filtered')
plt.plot(time_acc, -800 * np.sin(time_acc/5000) + np.random.normal(0, 200, samples), 
         'b-', alpha=0.5, linewidth=0.8, label='Raw')
plt.title("Acceleration", fontsize=10)
plt.ylabel("Amplitude")
plt.legend(fontsize=8, framealpha=1)
plt.gca().set_xticklabels([])  # Hide x-axis labels

# 2. Breathing Rate (Simplified)
plt.subplot(1, 3, 2)
plt.plot(time_others, 100 * np.sin(time_others/20000), 'g-', linewidth=1.5, label='Denoised')
plt.plot(time_others, 100 * np.sin(time_others/20000) + np.random.normal(0, 30, samples),
         'b-', alpha=0.5, linewidth=0.8, label='Noisy')
plt.title("Breathing Rate", fontsize=10)
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])

# 3. ECG Signal (Simplified)
plt.subplot(1, 3, 3)
ecg = 120 * np.sin(time_others/5000)**3
plt.plot(time_others, ecg, 'm-', linewidth=1.5, label='Denoised')
plt.plot(time_others, ecg + np.random.normal(0, 20, samples), 
         'b-', alpha=0.5, linewidth=0.8, label='Original')
plt.title("ECG Signal", fontsize=10)
plt.gca().set_xticklabels([])
plt.gca().set_yticklabels([])
plt.legend(fontsize=8, framealpha=1)

# Final adjustments
plt.tight_layout(pad=2.0)
plt.savefig('simple_signals_horizontal.png', dpi=150, bbox_inches='tight')
plt.show()