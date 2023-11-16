import serial
import time

serial_port = '/dev/ttyUSB0'
baud_rate = 57600


ser = serial.Serial(serial_port, baud_rate, timeout=1)
time.sleep(2)

commands = [
    "sys get ver\r\n",
    "radio set mod lora\r\n",
    "radio set freq 868000000\r\n",
    "radio set pwr 14\r\n",
    "radio set sf sf12\r\n",
    "radio set cr 4/8\r\n",
    "radio set bw 125\r\n",
    "radio tx 1589CCf\r\n"
]

# Send commands and read responses
for command in commands:
    ser.write(command.encode())
    response = ser.read(100)
    print("Command:", command.strip())
    print("Response:", response.decode().strip())
    print("------------")
    time.sleep(0.1)  # Add a delay between commands

# Close the serial connection
ser.close()
