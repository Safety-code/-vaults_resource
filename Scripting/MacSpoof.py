#!/bin/python3
#Subprocess module helps to execute system commands

from hashlib import new
import subprocess
import optparse

objparse = optparse.OptionParser()

objparse.add_option("-i", "--interface", dest="interface",help="Interface to change it's MAC address")

objparse.parse_args()
#optparse module helps to take userinput and pass them as arguments in the terminal

#interface  = "eth0"
interface = input("Enter the interface> ")
#newMAC= "00:11:22:33:44:77"
newMAC = input("Enter the New MAC address> ")
print ("[+] Changing MAC address for "+interface+ " to "+newMAC)

# subprocess.call("ifconfig "+interface+ " down", shell=True)
# subprocess.call("ifconfig "+interface+ " hw ether" +newMAC, shell=True)
# subprocess.call("ifconfig "+interface+ " up", shell=True)

#A more way of using the subprocess.call cammand, it's prevents users #from executing commands they are not permitted to
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether",newMAC] )
subprocess.call(["ifconfig", interface, "up"])
