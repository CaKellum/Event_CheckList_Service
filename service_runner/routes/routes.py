from ..app_container import app
from flask import render_template


@app.route("/")
def faq_route():
    ''' returns a rendered documentation '''
    return render_template("index.html")


def loaded_indicator():
    ''' This is an indecator to tell if routes have bee loaded'''
    print("routes are loaded")
