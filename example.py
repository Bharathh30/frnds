# import flast module
from flask import Flask,render_template

# instance of flask application
app = Flask(__name__)

# home route that returns below text when root url is accessed

@app.route("/")
def hello_world():
	return "<p>Hello, World!</p>"

@app.route("/manoj")
def manoj():
      render_template('home.html')

if __name__ == '__main__': 
    app.run(debug=True)
