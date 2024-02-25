import math
import time
import numpy as np
from rtlsdr import RtlSdr
import hackrf
from utils import cut_preamble, save_signal_old, read_file, write_file
from find_centers import SAMPLES_FOLDER


SAMPLE_RATE = 2_000_000


def capture_signal_rtlsdr():
    # Configure RTL-SDR parameters
    sdr = RtlSdr()
    sdr.sample_rate = SAMPLE_RATE
    #sdr.bandwitdh = 250000
    sdr.center_freq = 867937500
    sdr.gain = 5

    # Start signal capture
    capture_duration = 2.5  # in seconds

    print(f"Capturing signal for {capture_duration} seconds...")
    nb_samples = math.ceil(capture_duration * sdr.sample_rate /16384)*16384
    #samples = sdr.read_samples(5046272)
    samples = sdr.read_samples(nb_samples)
    
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

    # Start signal capture
    capture_duration = 2.5  # in seconds

    print(f"Capturing signal for {capture_duration} seconds...")
    nb_samples = math.ceil(capture_duration * hrf.sample_rate /16384)*16384
    samples = hrf.read_samples(nb_samples)
    
    hrf.close()
    samples = np.array(samples, dtype=np.complex64)
    return samples


if __name__ == "__main__":
    PREAMBLE_DURATION = 0.0245

    for i in range(2):
        while read_file('tmp.txt')[-1] != '0':
            print('recepteur is waiting')
            time.sleep(0.2)


        SIGNAL = capture_signal_rtlsdr()
        #SIGNAL = capture_signal_hackrf()
        PREAMBLE = cut_preamble(SIGNAL, 0.03, int(PREAMBLE_DURATION*SAMPLE_RATE))

        if len(PREAMBLE) > 0:
            save_signal_old(PREAMBLE,f'{SAMPLES_FOLDER}sample_{i+1}', np.complex64)
            print(f'signal {i+1} saved')
        else:
            print(f"no signal found for {i+1}")

        write_file('tmp.txt', '1')
