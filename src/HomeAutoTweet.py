#!/usr/bin/env python
import sys
import time
import datetime
import tweepy
from pyfirmata import Arduino, util
import django

DEBUGPRINT = True #toggles prints

#Version History
# - VERSION "1_000" - Original
VERSION = "1_001"   # Added Django
#--TWEEPY--
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'a8ENERDJCWMGX9sb2yfDUYo7c'
CONSUMER_SECRET = 'VhTJgkoQi4aV1kJtMwNQhELFPEZReMXNUIxrukipgN9N3tGO4g'
ACCESS_KEY = '26165501-CGVk57kq9LcBKVMb88eGL58mJrBX1Ga2SyiPUga0K'
ACCESS_SECRET = 'bvFKTkglUCw4LIMiWfc2JwnXEb1ZsAfq0PL4GSOYtH3JZ'

myapi = myauth = None

def TweepySetup(auth,consum_key, consum_sec, acc_key, acc_secret):
    try:
        #--Setup Tweepy
        Print_Wrpr("Setting up auth hndlr..")
        auth = tweepy.OAuthHandler(consum_key, consum_sec)
        Print_Wrpr("Setting up access token..")
        auth.set_access_token(acc_key, acc_secret)
        Print_Wrpr("Opening API..")
        #myapi = tweepy.API(auth)
        Print_Wrpr("Connecting to Arduino..")
        return tweepy.API(auth)
    
    except Exception as e:
        print "Exception "+e+" Occurred in Setup()"
        return None

    
def Print_Wrpr(str):
    if(DEBUGPRINT):
        print(str)
        
#==============
##### Main ####
#==============
Print_Wrpr("~ HomeAutoTest ~ Version "+VERSION+" ~")
Print_Wrpr("~ Django Version = "+django.get_version()+" ~")
Print_Wrpr("___________________________________")

myapi = TweepySetup(myauth,CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
if(myapi == None):
    Print_Wrpr("Setup Failed, Exiting...")
    sys.exit()
Print_Wrpr("Setup Complete!")
    
myboard = Arduino('/dev/ttyACM0')
Print_Wrpr("Arduino Tweety Setup SUCCESS..")
#make sure LED is OFF
myboard.digital[13].write(0)

#search through last 10 DMs
myDirectMsgs = myapi.direct_messages(count=10)
for status in myDirectMsgs:
    print " " + status.text + " by @" + status.sender.screen_name
    #myfile.write(" " + status.text + " by @" + status.sender.screen_name)
    if(status.text.find("TURN UP!")!=-1):
        print "\nTOO TURNT!"
        myboard.digital[13].write(1)
        break
    else:
        print "not so turnt :("    
Print_Wrpr("Exiting..")
Print_Wrpr("___________________________________")
    