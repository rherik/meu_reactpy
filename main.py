from reactpy import component, html
from reactpy.backend.flask import configure
from flask import Flask

@component
def hello_world():
    return html.h1("Hello, World!")

app = Flask(__name__)
configure(app, hello_world)