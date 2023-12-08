import time
from rtlsdr import RtlSdr

def capture_signal():
    # Configure RTL-SDR parameters
    sdr = RtlSdr()
    sdr.sample_rate = 250000
    #sdr.bandwitdh = 250000
    sdr.center_freq = 867937500
    sdr.gain = 2

    # Start signal capture
    start_time = time.time()
    capture_duration = 5  # in seconds
    samples = []

    print("Capturing signal for 5 seconds...")
    while (time.time() - start_time) < capture_duration:
        current_sample = sdr.read_samples(16384)
        samples.extend(current_sample)

    file_path = '../sample_data/received_signal.complex16s'
    print(f"Saving captured signal to {file_path}")
    with open(file_path, 'wb') as file:
        file.write(b''.join(samples))

    sdr.close()

if __name__ == "__main__":
    capture_signal()
