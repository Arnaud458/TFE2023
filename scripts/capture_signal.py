import math
import numpy as np
from rtlsdr import RtlSdr
from utils import cut_signal, save_signal, save_signal_old


def capture_signal():
    # Configure RTL-SDR parameters
    sdr = RtlSdr()
    sdr.sample_rate = 1000000
    #sdr.bandwitdh = 250000
    sdr.center_freq = 867937500
    sdr.gain = 0

    # Start signal capture
    capture_duration = 5  # in seconds

    print(f"Capturing signal for {capture_duration} seconds...")
    nb_samples = math.ceil(capture_duration * sdr.sample_rate /16384)*16384
    samples = sdr.read_samples(5046272)
    
    sdr.close()
    samples = np.array(samples, dtype=np.complex64)
    return samples


if __name__ == "__main__":
    TRESHOLD = 0.03
    SIGNAL = cut_signal(capture_signal(), TRESHOLD)
    #SIGNAL = capture_signal()
    if len(SIGNAL) > 0:
        save_signal_old(SIGNAL,'sample_data/test_64_misc', np.complex64)
        #save_signal(SIGNAL,'sample_data/test_64_misc', np.complex64)
        #save_signal_old(SIGNAL,'sample_data/test_256_1MHz', np.complex256)
    else:
        print("no signal found")
