import serial


SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 57600


ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)

commands = [
    "sys get ver\r\n",
    "radio set mod lora\r\n",
    "radio set freq 868000000\r\n",
    "radio set pwr 14\r\n",
    "radio set sf sf7\r\n",
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

# Close the serial connection
ser.close()
