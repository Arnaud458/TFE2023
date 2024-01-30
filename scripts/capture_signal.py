import math
import numpy as np
from rtlsdr import RtlSdr
from utils import cut_preamble, save_signal, save_signal_old

SAMPLE_RATE = 2_000_000

def capture_signal():
    # Configure RTL-SDR parameters
    sdr = RtlSdr()
    sdr.sample_rate = SAMPLE_RATE
    #sdr.bandwitdh = 250000
    sdr.center_freq = 867937500
    sdr.gain = 5

    # Start signal capture
    capture_duration = 4  # in seconds

    print(f"Capturing signal for {capture_duration} seconds...")
    nb_samples = math.ceil(capture_duration * sdr.sample_rate /16384)*16384
    samples = sdr.read_samples(5046272)
    #samples = sdr.read_samples(nb_samples)
    
    sdr.close()
    samples = np.array(samples, dtype=np.complex64)
    return samples


if __name__ == "__main__":
    TRESHOLD = 0.03
    PREAMBLE_DURATION = 0.01225
    
    SIGNAL = cut_preamble(capture_signal(), TRESHOLD, int(PREAMBLE_DURATION*SAMPLE_RATE))
    #SIGNAL = capture_signal()
    if len(SIGNAL) > 0:
        save_signal_old(SIGNAL,'preambules/1rn3', np.complex64)
        #save_signal(SIGNAL,'sample_data/test_64_misc', np.complex64)
        #save_signal_old(SIGNAL,'sample_data/test_256_1MHz', np.complex256)
    else:
        print("no signal found")
