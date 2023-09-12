from reactpy import component, html
from reactpy.backend.flask import configure
from flask import Flask

@component
def PrintButton(display_text, message_text):
    def handle_event(event):
        print(message_text)
    return html.button({"on_click": handle_event}, display_text)

@component
def button():
    return html.div(
                PrintButton("Play", "Playing"),
                PrintButton("Pause", "Paused"),
            )

app = Flask(__name__)
configure(app, button)
