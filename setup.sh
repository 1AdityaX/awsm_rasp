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

echo "Installing Python Libraries"

pip install -r requirements.txt

echo "Done!"

