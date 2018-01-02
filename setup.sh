#!/bin/bash

sudo apt-get update
sudo apt-get install git
sudo apt-get install uxterm
sudo git clone https://github.com/Mebus/cupp.git
cd cupp
sudo mv cupp3.py cupp.cfg ..
cd ..
sudo mv cupp3.py cupp.cfg sources
sudo rm -rf cupp
sudo apt-get install python3-pip
sudo pip3 install itertools
chmod +x creatwordlist.sh
