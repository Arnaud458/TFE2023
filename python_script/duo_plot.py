import numpy as np
import matplotlib.pyplot as plt

# Read the data from the file
data = np.fromfile('../sample_data/RN2483_1chirp.complex', dtype=np.complex64)
total_data = len(data)

# Separate the I/Q components from the original data
i = np.real(data)
q = np.imag(data)

# Plot the original I/Q samples
plt.figure(figsize=(8, 6))
plt.scatter(i, q, s=5, c='blue', alpha=0.5, label='Original')

# Differential interval (n)
n = 1
delta_f = 1

# Perform differential processing
differential_data = np.zeros_like(data)

for i in range(n, len(data)):
    phase_rotation = np.exp(-2j * np.pi * delta_f * n)
    differential_data[i] = data[i] * np.conj(data[i - n]) * phase_rotation

differential_i = np.real(differential_data)
differential_q = np.imag(differential_data)

# Plot
plt.scatter(differential_i, differential_q, s=5, c='red', alpha=0.5, label='Differential')
plt.xlabel('In-phase')
plt.ylabel('Quadrature')
plt.title('Original and Differential I/Q Samples')
plt.grid(True)
plt.legend()
plt.show()