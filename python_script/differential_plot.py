import numpy as np
import matplotlib.pyplot as plt

# Read the data from the file
data = np.fromfile('../sample_data/onechirp.complex', dtype=np.complex64)
total_data = len(data)

# Define the differential interval (n) and the frequency offset (delta_f)
n = 1
delta_f = 1

# Perform differential processing
differential_data = np.zeros_like(data)

for i in range(n, len(data)):
    phase_rotation = np.exp(-2j * np.pi * delta_f * n)
    differential_data[i] = data[i] * np.conj(data[i - n]) * phase_rotation

# Separate the differential I/Q components
differential_i = np.real(differential_data)
differential_q = np.imag(differential_data)

# Plot the differential I/Q samples
plt.figure(figsize=(8, 6))
plt.scatter(differential_i, differential_q, s=5, c='red', alpha=0.5)
plt.xlabel('Differential In-phase')
plt.ylabel('Differential Quadrature')
plt.title('Differential I/Q Samples')
plt.grid(True)
plt.show()