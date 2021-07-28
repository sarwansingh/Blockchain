from flask import *
import sqlite3

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html");

@app.route("/add")
def add():
	return render_template("add.html")

@app.route("/savedetails",methods = ["POST","GET"])
def saveDetails():
	msg = "msg"
	if request.method == "GET":
		try:
			sensorname    = request.args.get ("sensorname")
			temperature   = request.args.get("temperature")
			humidity      = request.args.get("humidity")
			msg =  sensorname + temperature+ " " + humidity
			with sqlite3.connect("sensor.db") as con:
				cur = con.cursor()
				#check the validity of data being send by user.
				cur.execute("INSERT into sensordata (sensorname, temperature, humidity) values (?,?,?)",(sensorname,temperature,humidity))
			
				con.commit()
				msg = " Sensor Data successfully Added "
		except:
			con.rollback()
			msg = " can not add the student to the list"
		finally:
			#return render_template("index.html", msg=msg )
			return " ",200
			con.close()

@app.route("/view")
def view():
	con = sqlite3.connect("sensor.db")
	con.row_factory = sqlite3.Row
	cur = con.cursor()
	cur.execute("select * from sensordata  order by timestamp desc")
	rows = cur.fetchall()
	return render_template("view.html",rows = rows)			
			
if  __name__ == "__main__":
	app.run( host="192.168.4.93",debug=True)
	