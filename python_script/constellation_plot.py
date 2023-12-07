import numpy as np
import matplotlib.pyplot as plt

data = np.fromfile('../sample_data/mini.complex16s', dtype=np.complex64)
total_data = len(data)
#print(total_data)
#for i in range(200):
#	print(data[i])
#cut = data[start:end]

i = np.real(data)
q = np.imag(data)

plt.figure(figsize=(8, 6))
plt.scatter(i, q, s=5, c='blue', alpha=0.5)
plt.xlabel('In-phase')
plt.ylabel('Quadrature')
plt.title('I/Q Samples')
plt.grid(True)
plt.show()