import sys
import numpy as np

from utils_display import display_density, display, display_quadrature
from utils import compute_differential, load_signal, DIFFERENTIAL_INTERVAL
from find_centers import find_highest_density_points


filename = 'sample_data/RN1/sample_1'
if len(sys.argv) > 2:
    filename = sys.argv[2]

if len(sys.argv) > 1:
    data = load_signal(filename, dtype=np.complex64)
    if sys.argv[1] == 'DISPLAY_SIGNAL':
        display(data)
    elif sys.argv[1] == 'DISPLAY_IQ':
        display_quadrature(data)
    elif sys.argv[1] == 'DISPLAY_DENSITY':
        display_density(compute_differential(data, DIFFERENTIAL_INTERVAL))    
    elif sys.argv[1] == 'DISPLAY_HDP':
        find_highest_density_points(data,True)
    else:
        print("INVALID ARGUMENT")
