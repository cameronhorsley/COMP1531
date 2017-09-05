from server import app, user_input
from flask import Flask, redirect, render_template, request, url_for, session

@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "POST":
		session['user_input'] = request.form["user_input"]
		return redirect(url_for("sort"))

	return render_template("index.html")

@app.route("/sort")
def sort():
	list = session.get('user_input', None).split(',')
	
	# Convert into integer list
	for x in range(0, len(list)):
		list[x] = int(list[x])
		
	to_print = []
	# to_print.append(str(list))

	# Bubble Sort list
	swapped = True
	while (swapped == True):
		swapped = False
	
		for x in range(1, len(list)):
			if (list[x-1] > list[x]) :
				list[x-1], list[x] = list[x], list[x-1]
				swapped = True
				to_print.append(str(list))
				
	return render_template("sort.html", to_print=to_print)
