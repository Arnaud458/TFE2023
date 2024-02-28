
import numpy as np
import os
from utils import rms_normalize, load_signal
from find_centers import SAMPLES_FOLDER


if __name__ == "__main__":

    dtype = np.complex64

    files = os.listdir(SAMPLES_FOLDER)

    samples = []
    for file in files:
        filepath = os.path.join(SAMPLES_FOLDER, file)  # Construct full file path
        sample = load_signal(filepath, dtype)
        samples.append(sample)

    # Normalize each sample individually
    normalized_samples = [rms_normalize(sample) for sample in samples]
    output_file = os.path.join(SAMPLES_FOLDER, file + "_normalized")

    # Save each normalized sample to a separate file
    for normalized_sample, output_file in zip(normalized_samples, files):
        normalized_sample.astype(np.complex64).tofile(output_file + "_normalized")