sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install git
sudo apt-get -y install python3-pip
sudo apt-get -y install python3
sudo apt-get -y dist-upgrade

echo "Installing Required Packages"

sudo apt-get install libhdf5-dev
sudo apt-get install libhdf5-serial-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev 

echo "Installing Python Libraries"

sudo python pip install -r requirements.txt

echo "Done!"

