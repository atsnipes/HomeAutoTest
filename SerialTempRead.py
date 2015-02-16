import serial
import time
import re

def extract_number(s):
    REGEX = '[-+]?[0-9]+(?:\.[0-9]+)?(?:[eE][-+]?[0-9]+)?' # matching any floating point$
    return re.findall(REGEX, s)

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
#===============================================================================
# PERIOD = "."
# ctr = 0
# while 1:
#     if ser.inWaiting():
#         val = ser.read(ser.inWaiting())
#         if PERIOD in val:
#             #temp_list = re.findall(r"[-+]?\d*\.\d+|d+",val)
#             temp_list = extract_number(val)
#             if(temp_list):
#                 print "Found Floats = "+str(temp_list)
#             else:
#                 print "No floats found"
#         else:
#             print "no period found, string  =  {"+val+" }"
#  #           print "split ="+str(val.split("."))
#         if(ctr<10):
#             ser.write("t\n")
#             ctr+=1
#             time.sleep(1)
#         else:
#             break
#    # time.sleep(1)
# 
# print "WE DONEZO"
# ser.close()
#===============================================================================

