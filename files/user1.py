from flask import Blueprint

page = Blueprint('page', __name__)

@page.route("/")
def main():
    return "Welcome user 1"
