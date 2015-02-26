import serial
import time
import re

def extract_number(s):
    regex = '[-+]?[0-9]+(?:\.[0-9]+)?(?:[eE][-+]?[0-9]+)?' # matching any floating point number 
    return re.findall(regex, s)

def rd_temp():
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
    time.sleep(1)
    ser.flush()
    ser.write("f\n")
    time.sleep(1)
    val = ser.read(ser.inWaiting())
    temp_list = extract_number(val)
    if(temp_list):
        print "Found Floats = "+str(temp_list)
    else:
        print "No floats found"
    ser.close()
