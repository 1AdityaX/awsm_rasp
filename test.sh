#!/bin/bash

user=$SUDO_USER
if [ -z "$user" ]; then 
    user=$USER
fi

startup_command="/usr/bin/python /home/pi/awsm_rasp/main.py"
if sudo -u "$user" crontab -l | grep -q "@reboot $startup_command"; then
    echo "[-] Cron Job already exists."
else
    tmp_file=$(sudo -u "$user" mktemp)
    echo "@reboot $startup_command" | sudo -u "$user" tee -a "$tmp_file" > /dev/null
    sudo -u "$user" crontab "$tmp_file"
    sudo -u "$user" rm "$temp_file"
    echo "[+] Cron job added successfully."
fi
