<<<<<<< HEAD
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template("index.html")

@app.route('/add_data', methods = ['POST'])
def add_data():
	if request.method == 'POST':
		name   = request.form['txtName']
		email  = request.form['txtEmail']
		coursename   = request.form['txtCourseName']
		return name+ email+ coursename
		
@app.route('/about')
def fabout():
	return '<html><h1>This is about page</h1><hr> <a href="/">Main Page</a></html> '
	
if __name__ == '__main__':
=======
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template("index.html")

@app.route('/add_data', methods = ['POST'])
def add_data():
	if request.method == 'POST':
		name   = request.form['txtName']
		email  = request.form['txtEmail']
		coursename   = request.form['txtCourseName']
		#save the entire data in database
		# or for any other processing
		return render_template("saveblk.html", name=name,email=email,coursename=coursename)  
		
@app.route('/about')
def fabout():
	return '<html><h1>This is about page</h1><hr> <a href="/">Main Page</a></html> '
	
if __name__ == '__main__':
>>>>>>> c48397b433d6dd08d8291445c33d93b17ab5ed61
	app.run(debug="true")