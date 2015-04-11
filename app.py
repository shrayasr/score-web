import re

import requests

from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def score():
    url = "http://www.espncricinfo.com/indian-premier-league-2015/engine/match/829711.html"
    page = requests.get(url)
    match = re.search(r"<title>.*</title>", page.text)
    title = match.group(0)
    return Response(title.split("|")[0].split(">")[1].strip(), mimetype="text/plain")


if __name__ == "__main__":
    app.run()

