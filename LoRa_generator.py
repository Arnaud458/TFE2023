import numpy as np

def generate_lora_signal(symbol_rate, bandwidth, spreading_factor, duration):
    samples_per_symbol = int(symbol_rate / bandwidth)
    total_samples = int(symbol_rate * duration)

    t = np.linspace(0, duration, total_samples)
    signal = np.zeros(total_samples, dtype=np.complex64)

    for i in range(total_samples):
        phase = 0
        for sf in range(spreading_factor):
            frequency = bandwidth * 2**(sf/spreading_factor)
            chirp_signal = np.exp(1j * 2 * np.pi * frequency * t[i])
            phase += chirp_signal

        signal[i] = phase / spreading_factor

    return signal

# Example usage
symbol_rate = 10000  # Symbol rate in Hz
bandwidth = 5000  # Bandwidth in Hz
spreading_factor = 10
duration = 1  # Duration in seconds

lora_signal = generate_lora_signal(symbol_rate, bandwidth, spreading_factor, duration)
