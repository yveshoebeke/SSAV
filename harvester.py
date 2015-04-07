import serial

ser = serial.Serial(1, 38400, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
#s = ser.read(100)       # read up to one hundred bytes
line = ser.readline()   # read a '\n' terminated line
