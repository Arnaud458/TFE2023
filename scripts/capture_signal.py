import math
import time
import numpy as np
from rtlsdr import RtlSdr
from utils import cut_preamble, save_signal, save_signal_old, read_file, write_file


SAMPLE_RATE = 2_000_000

def capture_signal():
    # Configure RTL-SDR parameters
    sdr = RtlSdr()
    sdr.sample_rate = SAMPLE_RATE
    #sdr.bandwitdh = 250000
    sdr.center_freq = 867937500
    sdr.gain = 0

    # Start signal capture
    capture_duration = 4  # in seconds

    print(f"Capturing signal for {capture_duration} seconds...")
    nb_samples = math.ceil(capture_duration * sdr.sample_rate /16384)*16384
    #samples = sdr.read_samples(5046272)
    samples = sdr.read_samples(nb_samples)
    
    sdr.close()
    samples = np.array(samples, dtype=np.complex64)
    return samples


if __name__ == "__main__":
    TRESHOLD = 0.03
    PREAMBLE_DURATION = 0.01225

    for i in range(3):
        while True:
            x = read_file('tmp.txt')[0]
            print('recepteur:', x)
            if x == '0':
                break
            time.sleep(0.1)


        SIGNAL = capture_signal()
        PREAMBLE = cut_preamble(SIGNAL, TRESHOLD, int(PREAMBLE_DURATION*SAMPLE_RATE))

        if len(PREAMBLE) > 0:
            save_signal_old(PREAMBLE,f'preambles/test_{i+1}', np.complex64)
            print(f'signal {i+1} saved')
        else:
            print(f"no signal found for {i+1}")

        write_file('tmp.txt', '1')
