sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get install -y python3
sudo apt-get install -y python3-pip
sudo apt-get install -y python-is-python3
sudo apt-get -y dist-upgrade

echo "Installing Required Packages"

sudo apt-get install -y libhdf5-dev
sudo apt-get install -y libhdf5-serial-dev
sudo apt-get install -y libatlas-base-dev
sudo apt-get install -y libjasper-dev 
sudo apt-get install -y libopenjp2-7
sudo apt-get install -y libavcodec-dev
sudo apt-get install -y libavformat-dev
sudo apt-get install -y libswscale-dev
sudo apt-get install -y libgtk-3-dev

echo "Installing Python Libraries"

pip install -r requirements.txt
pip install smbus-cffi --upgrade

echo "Done!"

