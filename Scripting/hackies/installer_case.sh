#!/bin/bash
# basic update and installation commands

errolog=/var/log/update_error.log
upgrade_errolog=/var/log/ugrade_error.log
clone_error=/var/log/clone_error.log
check_exit_status(){
	if [ $? -ne 0 ]	
	then
		echo "An error occured in your script, please check the $errorlog file"
	else
		echo "Your script runs successfully."
	fi
}

finished=0

while [ $finished -ne 1 ]
do
	echo "Select your option of action"

	echo "1 - Update "
	echo "2 - Upgrade"
	echo "3 - Update & Upgrade"
	echo "4 - Dist-Upgrade"
	echo "5 - Git clone"
	echo "6 - Install your package using apt"
	echo "7 - Install your package using dpkg"
	echo "8 - Exit"
	echo "* - Quit"


	read action;

	case $1 in
		1) echo " Update your system."
			sudo apt update 2>>$errolog
			check_exit_status
			;;

		2) echo "Upgrade your system."
			sudo apt upgrade 2>>$upgrade_errorlog
			check_exit_status
			;;

		3) echo "Update and Upgrade system altogether."
			sudo apt update && sudo apt -y full-upgrade
			check_exit_status
			;;

		4) echo "Upgrade your system to new dist version"
			sudo apt dist-upgrade
			check_exit_status
			;;

		5)echo "Clone your specified repo using git clone."
			echo "Enter url of the cloned repo."
			read repo
			git clone $repo 2>>$clone_error
			;;

		6) echo "Install package using apt"
			echo "Enter the name of the package you want to install"
			read package
			sudo apt install $package
			check_exit_status
			;;

		7) echo "Install your package using dpkg"
			echo "Enter the name of the package you want to install"
			read package
			sudo dpkg -i $package
			check_exit_status
			;;
		8) echo "Exit"
			;;

		*) echo "Exit"
			;;


	esac
done
