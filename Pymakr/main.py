import time
import pycom
from network import LoRa
import socket
import time

# initialise LoRa in LORA mode
lora = LoRa(mode=LoRa.LORA, frequency= 868000000, bandwidth=LoRa.BW_125KHZ, sf=12, preamble=6,
    coding_rate=LoRa.CODING_4_8)

# create a raw LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

#send data
s.setblocking(True)
s.send('Hello')
