from network import LoRa
import socket

# initialise LoRa in LORA mode
# Europe = LoRa.EU868

lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)

# create a raw LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

# send some data
s.setblocking(True)
s.send('Hello')