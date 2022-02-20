from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/form/")
def form():
    return render_template("form.html")

# On form submission we are redirected to the /success endpoint
@app.route("/success", methods = ["POST", "GET"])
def success():
   if request.method == "POST":
      name = request.form.get("Name")
      return render_template("success.html", name = name)
