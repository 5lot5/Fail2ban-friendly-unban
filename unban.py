#!/usr/bin/python

'''
   Script that makes unbanning clients from fail2ban more friendly

          written by 5lot5 - 5lot5 at telenet dot be
'''

import subprocess
import time

ip = ""
jail = ""

ip = raw_input ("What is the IP to unban? ")
while jail != "" or jail !="l":
      jail = raw_input ("\nWhat is the jail it's banned from? (l=list)")
      if jail == "l" or jail == "L":
         subprocess.call("sudo " + "fail2ban-client " + "status", shell = True)
      else:
         break
confirm = raw_input("\n\nContinue UNBAN "+ip+" from "+jail+"? (Y/N) ")
if confirm == "y" or confirm == "Y":
   cmd = ("sudo " + "fail2ban-client " + "set " + jail + " unbanip " + ip)
   subprocess.call(cmd, shell=True)
elif confirm == "n" or confirm == "N":
     exit("\nNothing done. Exiting.\n")
print "\nDone.\n"
