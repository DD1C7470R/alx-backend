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
def get_locale() -> str:
    """Retrieves the locale for a web page."""
    try:
        queries = request.args.to_dict()
        locale = queries.get('locale')
        if locale and locale in app.config["LANGUAGES"]:
            return locale
    except Exception as e:
        app.logger.error(f"Error processing request query parameters: {e}")

    # Resort to default behavior if locale not provided or invalid
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_indexi() -> str:
    """ Prints a Message when / is called """
    return render_template('0-index.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=2000)
