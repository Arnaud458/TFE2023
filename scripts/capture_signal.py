import math
import time
import numpy as np
from rtlsdr import RtlSdr
import hackrf
from utils import cut_preamble, save_signal, read_file, write_file
from find_centers import SAMPLES_FOLDER


SAMPLE_RATE = 2_000_000
CAPTURE_DURATION = 2.5 # in seconds


def compute_nb_samples():
    return math.ceil(CAPTURE_DURATION * SAMPLE_RATE /16384)*16384


def capture_signal_rtlsdr():
    # Configure RTL-SDR parameters
    sdr = RtlSdr()
    sdr.sample_rate = SAMPLE_RATE
    #sdr.bandwitdh = 250000
    sdr.center_freq = 867937500
    sdr.gain = 2

    print(f"Capturing signal for {CAPTURE_DURATION} seconds...")
    samples = sdr.read_samples(compute_nb_samples())
    
    sdr.close()
    samples = np.array(samples, dtype=np.complex64)
    return samples

def capture_signal_hackrf():
    # Configure hackrf parameters
    hrf = hackrf.HackRF()
    hrf.sample_rate = SAMPLE_RATE
    hrf.center_freq = 867937500
    #hrf.disable_amp()
    #hrf.lna_gain = 0
    #hrf.vga_gain = 0

    print(f"Capturing signal for {CAPTURE_DURATION} seconds...")
    samples = hrf.read_samples(compute_nb_samples())
    
    hrf.close()
    samples = np.array(samples, dtype=np.complex64)
    return samples


if __name__ == "__main__":
    PREAMBLE_DURATION = 0.098

    for i in range(12):
        while read_file('tmp.txt')[-1] != '0':
            print('recepteur is waiting')
            time.sleep(0.2)

        SIGNAL = capture_signal_rtlsdr()
        #SIGNAL = capture_signal_hackrf()
        PREAMBLE = cut_preamble(SIGNAL, 0.03, int(PREAMBLE_DURATION*SAMPLE_RATE))

        if len(PREAMBLE) > 0:
            save_signal(PREAMBLE,f'{SAMPLES_FOLDER}sample_{i+1}', np.complex64)
            print(f'signal {i+1} saved')
        else:
            print(f"no signal found for {i+1}")

        write_file('tmp.txt', '1')
