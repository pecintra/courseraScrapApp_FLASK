from flask import Flask, render_template, request, flash, send_file
from utils import course_identifier, get_courses

app = Flask(__name__)
app.secret_key = "coursera123"

@app.route("/")
def index():
	flash("Which field do you want to gather data from?")
	return render_template("index.html")

@app.route("/scrap", methods=['POST', 'GET'])
def scrap():
	render_template("index.html")
	category = request.form["coursesForm"]
	course = course_identifier(category)
	get_courses(course)
	return render_template("results.html")

@app.route("/download")
def download_file():
	download_path = 'coursera_info.csv'
	return send_file(download_path,as_attachment=True)


if __name__ == '__main__':
    app.run()
