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
	app.run(debug="true")