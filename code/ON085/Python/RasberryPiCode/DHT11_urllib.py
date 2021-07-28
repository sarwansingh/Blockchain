import Adafruit_DHT
import time, urllib.request
# Set sensor type : Options are DHT11,DHT22 or AM2302
sensor=Adafruit_DHT.DHT11
 
gpio=17
 
while True:
# Use read_retry method. This will retry up to 15 times to
# get a sensor reading (waiting 2 seconds between each retry).
    humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
 
# Reading the DHT11 is very sensitive to timings and occasionally
# the Pi might fail to get a valid reading. So check if readings are valid.
    if humidity is not None and temperature is not None:
      print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
      url ="http://192.168.4.93:5000/savedetails?"
      url = url + "sensorname=DHTr1"
      url = url + "&temperature="+str(temperature)
      url = url + "&humidity="+str(humidity)
      res = urllib.request.urlopen(url)
      time.sleep(3)
    else:
      print('Failed to get reading. Try again!')

