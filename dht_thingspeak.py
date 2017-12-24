# Sends temperature and humidity data to Thingspeak from a DHT sensor connected to Raspberry
# Requires Adafruit_DHT to be installed

# Sends data in every 10 mins:
# crontab -e
# */10 * * * * /usr/bin/python /home/pi/dht_thingspeak.py

# This code shows DHT11 connected to GPIO 23 (pin 16 on Rpi zero)
# tamasharasztosi, 2017

import sys
import Adafruit_DHT               # https://github.com/adafruit/Adafruit_Python_DHT
import urllib2

sensor  = 11                      # 11 : DHT11, 12 : DHT22, 2302: AM2302
pin     = 23                      # GPIO port on Raspberry
myAPI   = "FILL_WITH_YOUR_API"    # Write API of the channel

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
urllib2.urlopen(baseURL + "&field1=%s&field2=%s" % (temperature, humidity))
print('Data sent to Thingspeak')

if humidity is not None and temperature is not None:
    print('Temperature={0:0.1f} C  Humidity={1:0.1f} %'.format(temperature, humidity))
else:
    print('Failed to get reading. Try again!')
    sys.exit(1)
