#
# Hopefully an easy install script for SDL GroveWeatherPi
# and all required addon packages associated with it.
#
# You will still need to edit config.py in SDL_Pi_GroveWeatherPi folder 
# as well as import SQL dBase structure and edit WeeWx to pull fileparse data


#!/bin/sh
import sys
import math
import os


LIST_OF_APPS='python-smbus python-usb python-configobj python-cheetah python-imaging python-matplotlib python-pip gfortran libi2c-dev python-setuptools libblas-dev libatlas-base-dev liblapack-dev python-dev mysql-server python-mysqldb phpmyadmin'

os.system('ls')
print('Lets delete unused folders, dont worry, nothing important')
#input('Press Enter to continue...')

os.system('cd')
os.system('sudo rm -rf Documents  Downloads  Music  Pictures  python_games  Templates  Videos')

print('Ok, lets grab the required packages')
#input('Press Enter to continue...')

os.system('cd')
os.system('curl -s http://weewx.com/keys.html | sudo apt-key add -')
os.system('echo "deb [arch=all] http://weewx.com/apt/ squeeze main" | sudo tee /etc/apt/sources.list.d/weewx.list')
os.system('sudo apt-get update -y')
os.system("sudo apt-get install -y "+LIST_OF_APPS)
#
os.system('sudo apt-get install weewx')
#
os.system('cd')
os.system('sudo git clone https://github.com/switchdoclabs/SDL_Pi_GroveWeatherPi')
os.system('sudo git clone https://github.com/adafruit/Adafruit_Python_PureIO.git')
os.system('cd Adafruit_Python_PureIO')
os.system('sudo python setup.py install')
os.system('sudo pip install --upgrade setuptools pip')
os.system('sudo pip install setuptools --upgrade')
os.system('sudo pip install apscheduler')
#
os.system('cd')
os.system('sudo easy_install scipy -y')
os.system('sudo pip install tentacle_pi')
#
os.system('cd')
sys.exit()
