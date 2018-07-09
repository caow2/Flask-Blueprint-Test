from flask import Blueprint

page = Blueprint('user1_page', __name__)

@page.route("/")
def main():
    return "Welcome user 1"

@page.route("/hello/")
def hello():
    return "Hello World! (from user 1)"
