from flask import Flask, render_template, request, send_file
import os
from scrapper_py import scrape_freshersworld, save_to_excel  # Import scraper functions

app = Flask(__name__, static_folder="static")  # Ensure static files work

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        job_title = request.form["job_title"]
        location = request.form["location"]

        jobs = scrape_freshersworld(job_title, location)
        if jobs:
            filename = f"{job_title}_jobs_in_{location}.xlsx"
            save_to_excel(jobs, filename)
            return render_template("result.html", filename=filename)
        else:
            return render_template("result.html", error="No jobs found!")

    return render_template("index.html")

@app.route("/download/<filename>")
def download_file(filename):
    file_path = os.path.join(os.getcwd(), filename)
    return send_file(file_path, as_attachment=True, mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

if __name__ == "__main__":
    app.run(debug=True)
