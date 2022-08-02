
from socket import timeout
import serial
from serial import Serial

ser = serial.Serial('COM5', 9600, timeout=1)
# ser.open()
# ser.is_open
data = ser.readline()
print(data)
# ser.close()