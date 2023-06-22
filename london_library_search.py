from flask import Flask, render_template, request, url_for
from app.search import Search
from app.catalogues import catalogues

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def home():
    return render_template("home.html", boroughs=catalogues.keys())


@app.route("/search", methods = ["POST"])
def search():
    query_text = request.form["query"]
    boroughs = request.form.getlist("boroughs")
    borough_checks = {borough: borough in boroughs for borough in catalogues.keys() }
    return render_template("search_results.html", borough_checks=borough_checks, query=query_text, results=Search(query_text, boroughs, 10).get_results())


# Favicon paths, should be in root but flask needs them in static so reroute.
@app.route('/android-chrome-192x192.png')
def android_chrome_192():
    return app.send_static_file('android-chrome-192x192.png')
@app.route('/android-chrome-256x256.png')
def android_chrome_256():
    return app.send_static_file('android-chrome-256x256.png')
@app.route('/apple-touch-icon.png')
def apple_touch_icon():
    return app.send_static_file('apple-touch-icon.png')
@app.route('/browserconfig.xml')
def browser_config():
    return app.send_static_file('browserconfig.xml')
@app.route('/favicon.ico')
def favicon_ico():
    return app.send_static_file('favicon.ico')
@app.route('/favicon-16x16.png')
def favicon_16():
    return app.send_static_file('favicon-16x16.png')
@app.route('/favicon-32x32.png')
def favicon_32():
    return app.send_static_file('favicon-32x32.png')
@app.route('/mstile-150x150.png')
def mstile_150():
    return app.send_static_file('mstile-150x150.png')
@app.route('/safari-pinned-tab.svg')
def safari_pinned_tab():
    return app.send_static_file('safari-pinned-tab.svg')
@app.route('/site.webmanifest')
def site_webmanifest():
    return app.send_static_file('site.webmanifest')


if __name__ == "__main__":
    app.run()
