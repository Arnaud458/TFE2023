import serial
import time
from utils import read_file, write_file

SERIAL_PORT = '/dev/ttyUSB0'
BAUD_RATE = 57600
SPREADING_FACTOR = 8

config_commands = [
    "sys get ver\r\n",
    "radio set mod lora\r\n",
    "radio set freq 868000000\r\n",
    "radio set pwr 14\r\n",
    f"radio set sf sf{SPREADING_FACTOR}\r\n",
    "radio set cr 4/8\r\n",
    "radio set bw 125\r\n"
]

MESSAGE_COMMAND = "radio tx 1509ACf\r\n"


def config(ser: serial.Serial):
    # Send commands and read responses
    for command in config_commands:
       write_command(ser, command)


def send_signal(ser: serial.Serial):
    write_command(ser, MESSAGE_COMMAND)


def write_command(ser: serial.Serial, command: str):
    ser.write(command.encode())
    response = ser.read(100)
    print("Command:", command.strip())
    print("Response:", response.decode().strip())
    print("------------")


if __name__ == '__main__':
    SER = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    for i in range(25):
        #time.sleep(1)
        config(SER)
        write_file('tmp.txt','0')
        time.sleep(1.5)
        send_signal(SER)
        while read_file('tmp.txt')[-1] != '1':
            print('emmeteur is waiting')
            time.sleep(1)
    #config(SER)
    #send_signal(SER)
    SER.close()

    
