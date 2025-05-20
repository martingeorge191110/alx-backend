#!/usr/bin/env python3
"""basic Flask app with one route"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home() -> str:
    """html page"""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
