from flask import Flask, redirect, render_template, request, url_for
from server import app, user_input
import csv
def csv_write(name, zID, description):
	with open('user_info.csv', 'a') as csv_out:
		writer = csv.writer(csv_out)
		writer.writerow([name, zID, description])
		
def csv_read():
	with open('user_info.csv', 'r') as csv_in:
		reader = csv.reader(csv_in)
		csv_input = []
		for row in reader:
			csv_input.append(row)
		return csv_input
			
@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		name = request.form["name"]
		zID = int(request.form["zID"])
		description = request.form["desc"]
		
		csv_write(name, zID, description)

		return redirect(url_for("hello"))
	return render_template("index.html")



@app.route("/hello")
def hello():
	csv_input = csv_read()
	return render_template("hello.html", csv_input=csv_input)
    
@app.route("/hello/<name>")
def user(name):
	
	return render_template("user.html", name=name)
    

