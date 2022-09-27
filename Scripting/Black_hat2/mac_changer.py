#import optpars
from email import parser
import subprocess
import optparse

# Parser for handling command-line argument
parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface",  help="Interface to change its MAC address")
parser.add_option("-m", "--mac", dest="new_mac",  help="New MAC Address")

(options, arguments) = parser.parse_args()

# interface = input("Interface > ")
# new_MAC = input("New MAC > ")

interface = options.interface
new_MAC = options.new_mac

print("[+] Changing MAC address for " + interface + " to " + new_MAC)

# subprocess.calll("ifconfig"+ interface+ "down", shell=  True)
# subprocess.call("ifconfig"+ interface+ "hw ether"+ new_MAC, shell=  True)
# subprocess.call("ifconfig"+ interface+ "up", shell=  True)

# More secure way of writing the command above
subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_MAC])
subprocess.call(["ifconfig", interface, "up"])