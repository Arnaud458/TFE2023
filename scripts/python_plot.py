import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import chirp

# Define time array
t = np.linspace(0, 1, 1000)

# Define chirp signal parameters
f_start = 10  # Start frequency of the chirp signal (10 Hz)
f_end = 100   # End frequency of the chirp signal (100 Hz)

# Create chirp signal
chirp_signal = chirp(t, f0=f_start, f1=f_end, t1=1, method='linear')

# Calculate instantaneous frequency
instantaneous_frequency = np.gradient(np.unwrap(np.angle(chirp_signal)), t)

# Plot the signals
plt.figure(figsize=(10, 8))

# Plot waveform
plt.subplot(2, 1, 1)
plt.plot(t, chirp_signal, 'b')
plt.title('Chirp Signal')
plt.xlabel('Time')
plt.ylabel('Amplitude')

# Plot instantaneous frequency
plt.subplot(2, 1, 2)
plt.plot(t, instantaneous_frequency, 'r')
plt.title('Instantaneous Frequency')
plt.xlabel('Time')
plt.ylabel('Frequency (Hz)')

plt.tight_layout()
plt.show()