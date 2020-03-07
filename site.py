from flask import Flask, render_template, request
import requests

app = Flask("PortfolioSite")

@app.route("/")
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

@app.route("/contact")
def contact():
        return render_template("contact.html")

app.run(port=5001)