#!/usr/bin/env python3
"""the babel instance module"""

from flask_babel import Babel
from flask import Flask, render_template, request


app = Flask(__name__)
babel = Babel(app)


class Config:
    """configuration class for babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Use request.accept_languages to determine the best
    match with our supported languages"""
    locale = request.args.get("locale", None)
    if locale is not None and locale in app.config["LANGUAGES"]:
        print(locale)
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/', methods=["GET"], strict_slashes=False)
def hello():
    """
    hello.
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
