import numpy as np


DIFFERENTIAL_INTERVAL = 15
FREQUENCY_OFFSET = -62500


def read_file(filename: str):
    with open(filename, 'r',encoding='utf8') as reader:
        return reader.readlines()

def write_file(filename: str, content: str):
    with open(filename, 'a',encoding='utf8') as writer:
        writer.write('\n' +content)

def compute_differential(
        data: np.ndarray,
        differential_interval: int=DIFFERENTIAL_INTERVAL,
        frequency_offset: int=FREQUENCY_OFFSET
    ) -> np.array:

    differential_data = np.zeros_like(data)

    for i in range(differential_interval, len(data)):
        phase_rotation = np.exp(-2j * np.pi * frequency_offset * differential_interval)
        differential_data[i] = data[i] * np.conj(data[i - differential_interval]) * phase_rotation
        # differential_data[i] = DATA[i] * np.conj(DATA[i - n]) * np.exp(-1j * 2 * np.pi * delta_f * n)

    return differential_data


def save_signal_old(signal, filepath, dtype):
    signal_to_save = np.array(signal, dtype=dtype)
    print(f"Saving captured signal to {filepath}")
    with open(filepath, 'wb') as file:
        file.write(b''.join(signal_to_save))


def save_signal(signal: np.ndarray, filepath: str, dtype) -> None:
    signal_to_save = np.array(signal, dtype=dtype)
    print(f"Saving captured signal to {filepath}.npz")
    np.savez_compressed(filepath, signal_to_save)


def load_signal(filepath: str, dtype) -> np.ndarray:
    if filepath.endswith('.npz'):
        return np.load(filepath)['arr_0']
    return np.fromfile(filepath, dtype=dtype)


def old_cut_signal(signal, treshold):
    start_index = 0
    end_index = len(signal) - 1
    consecutive_start = 0
    consecutive_end = 0
    while start_index < len(signal) and consecutive_start <3:
        if abs(np.real(signal[start_index])) > treshold or abs(np.imag(signal[start_index])) > treshold:
            consecutive_start += 1
        else :
            consecutive_start = 0
        start_index += 1

    while end_index > start_index and consecutive_end < 3:
        if abs(np.real(signal[end_index])) > treshold or abs(np.imag(signal[end_index])) > treshold:
            consecutive_end += 1
        else :
            consecutive_end = 0
        end_index -= 1

    if start_index == end_index:
        return []

    return signal[start_index:end_index]


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