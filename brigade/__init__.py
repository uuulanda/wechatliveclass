import os

from flask import Blueprint, Flask, render_template
from .sitemap import sitemap_blueprint
from flask_webpack import Webpack
from filters import filters

brigade = Blueprint('brigade', __name__)

def detect_webpack_manifest_path(expected_path):
    path = os.path.abspath(expected_path)
    if os.path.exists(path):
        return path
    else:
        raise Exception("Webpack Build Missing -- Make sure webpack is running. " \
                "Start it with `webpack --watch`")


def create_app():
    app = Flask(__name__, static_folder='build/public/', static_url_path='/assets')
    app.config['SECRET_KEY'] = 'sekrit!'
    app.config['WEBPACK_MANIFEST_PATH'] = detect_webpack_manifest_path('./brigade/