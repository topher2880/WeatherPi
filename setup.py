#
# Hopefully an easy install script for SDL GroveWeatherPi
# and all required addon packages associated with it.
#
# You will still need to edit config.py in SDL_Pi_GroveWeatherPi folder 
# as well as import SQL dBase structure and edit WeeWx to pull fileparse data


#!/bin/sh
import sys
import math


LIST_OF_APPS="python-smbus python-matplotlib python-pip gfortran libi2c-dev python-setuptools libblas-dev libatlas-base-dev liblapack-dev python-dev mysql-server python-mysqldb phpmyadmin"

print('cd')
print('sudo apt-get update -y')
print('sudo apt-get install -y $LIST_OF_APPS')

print('sudo apt-get update -y')

print('cd')
print('sudo git clone https://github.com/topher2880/SDL_Pi_GroveWeatherPi')
print('sudo git clone https://github.com/adafruit/Adafruit_Python_PureIO.git')
print('cd Adafruit_Python_PureIO')
print('sudo python setup.py install')
print('cd')

print('sudo easy_install scipy -y')
print('sudo pip install tentacle_pi')

