# Dht raspberry thingspeak
#### Sends temperature and humidity data to Thingspeak from a DHT sensor connected to Raspberry

*Requires Adafruit_DHT to be installed: https://github.com/adafruit/Adafruit_Python_DHT*

Basic usage(after configuration):

> python dht_thingspeak.py

Sends data in every 10 mins:

> crontab -e

> */10 * * * * /usr/bin/python /home/pi/dht_thingspeak.py

This code shows DHT11 connected to GPIO 23 (pin 16 on Rpi zero)


*tamasharasztosi, 2017*
