#!/bin/bash

TODAY=$(date)
echo "Script is being run today: $TODAY"

clear
echo "
Please Select:

1. Update your system
2. Install package using  dpkg 
3. Install package using apt
4. Clone Github repository
5.Quit
"
read -p "Enter Selection [0-5] "

case "$REPLY" in
	0)	echo "Program terminated successfully."
		exit
		;;
	1)	echo "Updating System......!"
		sudo apt update
		;;
	2)	echo "Installing .deb package.....!"
		sudo dpkg -i $*.deb
		;;
	3)	echo "Installing package.....!"
		sudo apt install $1
		;;
	4)	echo "Cloning repo....!"
		git clone $1
		;;
	*)	echo "Invalid Entry" >&2
		exit 1
		;;
esac
