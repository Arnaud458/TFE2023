import numpy as np


DIFFERENTIAL_INTERVAL = 65536


def read_file(filename: str):
    with open(filename, 'r',encoding='utf8') as reader:
        return reader.readlines()

def write_file(filename: str, content: str):
    with open(filename, 'a',encoding='utf8') as writer:
        writer.write('\n' +content)

def compute_differential(
        data: np.ndarray,
        differential_interval: int=DIFFERENTIAL_INTERVAL
    ) -> np.array:

    differential_data = np.zeros(data.shape[0]-differential_interval, dtype= data.dtype)

    for i in range(data.shape[0] - differential_interval):
        a = np.real(data[i])
        b = np.imag(data[i])
        c = np.real(data[i+differential_interval])
        d = np.imag(data[i+differential_interval])
        differential_data[i] = a * c + b * d + 1j * (b * c - a *d)

    return differential_data


def save_signal(signal, filepath, dtype):
    signal_to_save = np.array(signal, dtype=dtype)
    print(f"Saving captured signal to {filepath}")
    with open(filepath, 'wb') as file:
        file.write(b''.join(signal_to_save))


def load_signal(filepath: str, dtype) -> np.ndarray:
    if filepath.endswith('.npz'):
        return np.load(filepath)['arr_0']
    return np.fromfile(filepath, dtype=dtype)


def cut_preamble(signal, treshold, preamble_size):
    start_index = 0
    consecutive_start = 0
    while start_index < len(signal) and consecutive_start <3:
        if abs(np.real(signal[start_index])) > treshold or abs(np.imag(signal[start_index])) > treshold:
            consecutive_start += 1
        else :
            consecutive_start = 0
        start_index += 1

    if start_index + preamble_size > len(signal) -1:
        return []

    return signal[start_index:start_index+preamble_size]

def rms_normalize(samples: np.ndarray) -> np.ndarray:
    rms_values = np.sqrt(np.mean(np.abs(samples)**2, axis=0))  # Compute RMS values
    normalized_samples = samples / rms_values  # Normalize samples
    return normalized_samples
