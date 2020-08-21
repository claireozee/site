import os
from flask import Flask, render_template, request, send_from_directory
import requests

app = Flask("PortfolioSite")

@app.route("/")
#@app.route("/", methods=['GET'])
def home():
        return render_template("home.html")

@app.route("/creative")
def creative():
        return render_template("creative.html")

@app.route("/experience")
def experience():
        return render_template("experience.html")

@app.route("/projects")
def projects():
        return render_template("projects.html")

@app.route("/blog")
def blog():
        return render_template("blog.html")

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               #'favicon.ico', mimetype='image/vnd.microsoft.icon')
                               'favicon.ico', mimetype='image/png')
 
#app.run(port=5002)
app.run(debug=True)