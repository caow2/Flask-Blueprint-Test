from flask import Blueprint

page = Blueprint('user2_page', __name__)

@page.route("/")
def main():
    return "Welcome user 2"

@page.route("/hello/")
def hello():
    return "Hello World! (from user 2)"
