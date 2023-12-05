import numpy as np
import matplotlib.pyplot as plt

# Read the data from the file
data = np.fromfile('onechirp.complex', dtype=np.complex64)
total_data = len(data)

# Separate the I/Q components from the original data
i = np.real(data)
q = np.imag(data)

# Plot the original I/Q samples
plt.figure(figsize=(8, 6))
plt.scatter(i, q, s=5, c='blue', alpha=0.5, label='Original')  # Original samples in blue

# Define the differential interval (n)
n = 1  # Adjust this value based on your signal's characteristics

# Perform differential processing
differential_data = np.zeros_like(data)  # Create an array to store differential data

for idx in range(n, len(data)):
    differential_data[idx] = data[idx] * np.conj(data[idx - n])  # Perform the differential operation

# Separate the differential I/Q components
differential_i = np.real(differential_data)
differential_q = np.imag(differential_data)

# Plot the differential I/Q samples
plt.scatter(differential_i, differential_q, s=5, c='red', alpha=0.5, label='Differential')  # Differential samples in red

# Plot settings
plt.xlabel('In-phase')
plt.ylabel('Quadrature')
plt.title('Original and Differential I/Q Samples')
plt.grid(True)
plt.legend()
plt.show()