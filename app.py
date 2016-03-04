# -*- coding: utf-8 -*-
"""
    Hello, World!
    ~~~~~~~~~~~~~

    An example app showing the basic use of Flask with templates.

    :copyright: (c) 2016 by bmcculley.
    :license: MIT, see LICENSE for more details.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("home.html")

if __name__ == "__main__":
	app.run()