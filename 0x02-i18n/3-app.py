#!/usr/bin/env python3
""" Starts a Flash Web Application """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Represents a Flask Babel configuration.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.url_map.strict_slahes = False
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> any:
    """get language local"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def get_indexi() -> str:
    """ Prints a Message when / is called """
    return render_template('0-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=2000)
