import time, urllib.request
temp=23
hum=50
sname="dht11"

url ="http://127.0.0.1:5000/savedetails?"

#sensorname=dht11&temperature=21&humidity=67"
for i in range (5) :
	url ="http://127.0.0.1:5000/savedetails?"
	url = url + "sensorname="+sname
	url = url + "&temperature="+str(temp)
	url = url + "&humidity="+str(hum)
	temp=temp+1
	hum = hum+2
	res = urllib.request.urlopen(url)
	print(res)
	print( url)
	time.sleep(2)