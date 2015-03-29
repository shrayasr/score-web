import re

import requests

from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def score():
    url = "http://www.espncricinfo.com/icc-cricket-world-cup-2015/engine/match/656495.html"
    page = requests.get(url)
    match = re.search(r"<title>.*</title>", page.text)
    title = match.group(0)
    return Response(title.split("|")[0].split(">")[1].strip(), mimetype="text/plain")


if __name__ == "__main__":
    app.run()

