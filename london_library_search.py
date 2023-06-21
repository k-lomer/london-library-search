from flask import Flask, render_template, request
from app.search import Search
from app.catalogues import catalogues

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", boroughs=catalogues.keys())

@app.route("/search", methods = ["POST"])
def search():
    query_text = request.form["query"]
    boroughs = request.form.getlist("boroughs")
    borough_checks = {borough: borough in boroughs for borough in catalogues.keys() }
    return render_template("search_results.html", borough_checks=borough_checks, query=query_text, results=Search(query_text, boroughs, 10).get_results())

if __name__ == "__main__":
    app.run()