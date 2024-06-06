# User Guide for analysis display

## Setup


### Create virtual environment (Optional)

### Install required libraries
`pip install -r requirements.txt`


## How to use

### Emit, listen and save signals (requires emission module and SDR !)

`bash emit_and_listen_signal.sh`

### Display captured signal I and Q samples

`python3 main.py DISPLAY_SIGNAL filepath`

for example :
`python3 main.py DISPLAY_SIGNAL sample_data/RN1/sample_1` 
will display the I and Q samples for the first sample (sample_1) of the module #1 (RN1)

### Display captured signal I samples as a function of Q samples

`python3 main.py DISPLAY_IQ filepath`

### Display density of the DCTF generated from the captured signal

`python3 main.py DISPLAY_DENSITY filepath`

### Display density of the DCTF generated from the captured signal

`python3 main.py DISPLAY_HDP filepath`

### Noramlize the samples of the current folder

`python3 normalize.py`

### Compute center of the DCTF generated from the captured signal

`python3 find_centers.py`
You need to manually change the target folder in pot_centers.py (line 74)

### Display the centers of the DCTF from all generated signals

`python3 plot_centers.py`
You may need to edit centers.json because it may contain data from previous experimentations
