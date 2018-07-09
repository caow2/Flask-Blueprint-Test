from flask import Flask
import sys
import glob
import os

#Instead of doing all the imports for the blueprints manually
#Automate the imports and the register_blueprints
#A dictionary is needed to access each specific module that was imported
os.chdir('./files/')
sys.path.append(os.getcwd())

app = Flask(__name__)

module_dict = {}
for file in glob.glob('*.py'):
    name = file[:-3] #excludes .py
    module = __import__(name)
    module_dict[name] = module

for key in module_dict:
    app.register_blueprint(module_dict[key].page, url_prefix='/%s' % key) #i.e '/user1'

@app.route('/')
def homepage():
    output = "<h1>Available pages that are currently available are:</h1>"
    output += "<p><a href='/user1/'>/user1/</a><br>"
    output += "<a href='/user1/hello/'>/user1/hello/</a></p>"
    output += "<p><a href='/user2/'>/user2/</a><br>"
    output += "<a href='/user2/hello/'>/user2/hello/</a></p>"
    return output

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
