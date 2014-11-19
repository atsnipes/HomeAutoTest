#!/usr/bin/env python
from pyfirmata import Arduino, util
import sys
import time
import datetime
import tweepy
raw_input("press enter")
board = Arduino('/dev/ttyACM0')
raw_input("board setup, press enter")
#digital_13 = board.get_pin('d:3:p')
while(1):
    strPSelect = raw_input("select pin")
    pin_select = int(strPSelect)
    strOpSelect = raw_input("select 0,1")
    if(strOpSelect != '0' and strOpSelect != '1'):
        print "Closing now..."
    else:
        OpSel = int(strOpSelect)
        board.digital[pin_select].write(OpSel)
        print "wrote to digital[ "+str(pin_select)+" ] = "+str(OpSel)
    
    
    #if(strOpSelect != '0' and strOpSelect != '1'):
       # break
   # if(strOpSelect == '1'):
      #  board.digital[pin_select].write(1)
        #digital_13.write(.5)
    #print "writing to digital["+str(pin_select)+"] = "+str()
    #board.digital[pin_select].write(op)
     
print "Exiting..."
