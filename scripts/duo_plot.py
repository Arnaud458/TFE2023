import numpy as np
from utils import compute_differential, load_signal
from utils_display import display_quadrature


DATA = load_signal('sample_data/test_64_1MHz', dtype=np.complex64)


display_quadrature((DATA, 'data'), (compute_differential(DATA), 'differential'))
