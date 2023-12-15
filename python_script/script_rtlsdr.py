import math
import numpy as np
from rtlsdr import RtlSdr

TRESHOLD = 0.01


def capture_signal():
    # Configure RTL-SDR parameters
    sdr = RtlSdr()
    sdr.sample_rate = 250000
    #sdr.bandwitdh = 250000
    sdr.center_freq = 867937500
    sdr.gain = 0

    # Start signal capture
    capture_duration = 5  # in seconds

    print(f"Capturing signal for {capture_duration} seconds...")
    nb_samples = math.ceil(capture_duration * sdr.sample_rate /16384)*16384
    samples = sdr.read_samples(nb_samples)
    
    sdr.close()
    return samples


def write_signal(signal):
    file_path = '../sample_data/received_signal.complex'
    print(f"Saving captured signal to {file_path}")
    with open(file_path, 'wb') as file:
        file.write(b''.join(signal))


def cut_signal(signal, treshold):
    start_index = 0
    end_index = len(signal)-1
    consecutive_start = 0
    consecutive_end = 0
    while consecutive_start <3:
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


if __name__ == "__main__":
    SIGNAL = cut_signal(capture_signal(),TRESHOLD)
    if len(SIGNAL) > 0:
        write_signal(SIGNAL)
    else:
        print("nothing")
