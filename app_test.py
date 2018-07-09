from flask import Flask
import files.user1
import files.user2
import sys

app = Flask(__name__)
app.register_blueprint(files.user1.page, url_prefix='/user1')
app.register_blueprint(files.user2.page, url_prefix='/user2')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
