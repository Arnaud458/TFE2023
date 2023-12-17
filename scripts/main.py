import numpy as np
from utils import cut_signal, save_signal


if __name__ == "__main__":
    # DATA = np.fromfile('sample_data/test_128', dtype=np.complex128)
    # print(type(DATA))
    # DATA = cut_signal(DATA[500:], 0.01)
    # print(type(DATA))

    # save_signal(DATA, "sample_data/test_128_cut_numpy_savez_compressed", dtype=np.complex128)

    # save_signal(DATA, 'sample_data/test_64_cut', dtype=np.complex64)

    DATA = np.load('sample_data/test_128_cut_numpy_savez_compressed.npz')

    print(type(DATA))

    print(type(DATA['arr_0']))

    print(type(DATA['arr_0'][0]))
