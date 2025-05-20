#!/usr/bin/env python3
"""basic Flask app with single route"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """flask babel configuration"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """returns the locale of a web page"""
    langs = {"en": "en", "fr": "fr"}
    if request.args.get('locale'):
        locale = request.args.get('locale')
        if locale in langs:
            return langs[locale]
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def home() -> str:
    """render 4-index.html page"""
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
