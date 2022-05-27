# AWSM rpi 

### Installation
```
 git clone https://github.com/AnonymousXsn/sd_rasp.git
```
### Setup
```
bash setup.sh
```
### Running the main script on startup

**1. open your .bashrc file**
```
nano .bashrc
```

**2. Add this piece of code at the end of your .bashrc file**

```
if [ -z "${SSH_TTY}" ]; then
  python /home/pi/sd_rasp/main.py
fi
```
# 
# End 

