import time
from rtlsdr import RtlSdr

def capture_signal():
    # Configure RTL-SDR parameters
    sdr = RtlSdr()
    sdr.sample_rate = 2000000  # Sample rate (Hz)
    sdr.center_freq = 868125000  # Center frequency (Hz)
    sdr.gain = 60        # Automatic gain control

    # Start signal capture
    start_time = time.time()
    capture_duration = 15  # Duration to capture in seconds
    samples = []

    print("Capturing signal for 15 seconds...")
    while (time.time() - start_time) < capture_duration:
        current_sample = sdr.read_samples(65536)  # Adjust the number of samples per iteration
        samples.extend(current_sample)

    # Save the captured signal to a file
    file_path = '../sample_data/received_signal.complex'
    print(f"Saving captured signal to {file_path}")
    with open(file_path, 'wb') as file:
        file.write(b''.join(samples))

    # Close the RTL-SDR device
    sdr.close()
    print("Signal capture complete.")

if __name__ == "__main__":
    capture_signal()
