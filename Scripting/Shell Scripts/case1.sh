#!/bin/bash
#Practice if case
# read-menu

clear
echo "
Please Select:

1. Display System Information
2. Display Disk Space
3. Display Home Space Utilization
4. Install A Package
5. Quit
"
read -p "Enter Selection [0-5] "

case "$REPLY" in
    0)  echo "Program terminated."
        exit
        ;;
    1)  echo "Hostname: $HOSTNAME"
        uptime
        ;;
    2)  df -h 
        ;;
    3)  if [[ "$(id -u)" -eq 0 ]]; then
            echo "Home Space Utilization (All users)"
            du -sh /home/*
        else
            echo "Home Space Utilization(Users)"
            du -sh $HOME
        fi
        ;;

    4)  echo "Updating System ................!"
        sudo apt install $1
        ;;
    *)  echo "Invalid entry" >&2
        exit 1
        ;;

esac  