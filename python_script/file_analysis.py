import numpy as np
import matplotlib.pyplot as plt

FILEPATH = '../sample_data/received_signal.complex'
DATATYPE = np.complex_

def read_file(filepath, datatype):
    return np.fromfile(filepath, dtype=datatype)

    

def display_quadrature(data):

    i = np.real(data)
    q = np.imag(data)

    plt.figure(figsize=(8, 6))
    plt.scatter(range(len(i)), i, s=5, c='orange', alpha=0.5)
    plt.scatter(range(len(i)), q, s=5, c='blue', alpha=0.5)
    plt.xlabel('In-phase')
    plt.ylabel('Quadrature')
    plt.title('I/Q Samples')
    plt.grid(True)
    plt.show()

    print(*data[:10],sep='\n')
    print('----------------------')
    print(*data[-10:],sep='\n')


if __name__ == "__main__":
    display_quadrature(read_file(FILEPATH, DATATYPE))