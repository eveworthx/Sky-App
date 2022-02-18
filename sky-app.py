from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello! Welcome to my web app</p>"

@app.route("/form/")
def form():
    return render_template('form.html')

@app.route('/success', methods = ['POST', 'GET'])
def success():
   if request.method == 'POST':
      success = request.form
      return render_template("success.html", success = success)