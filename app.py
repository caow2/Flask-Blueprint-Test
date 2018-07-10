from flask import Flask
import sys
import glob
import os
import fnmatch

#Instead of doing all the imports for the blueprints manually
#Automate the imports and the register_blueprints
#A dictionary is needed to access each specific module that was imported
os.chdir('./blueprints/')

app = Flask(__name__)

module_dict = {}
#loop thru all subdirs in blueprints and import all .py files
for dirName, subdirList, fileList in os.walk('.'): 
    sys.path.append(dirName) #if the directory is not in sys.path, python doesn't know where to import from
    for file in fileList:
        if fnmatch.fnmatch(file, '*.py'):
            name = file[:-3]
            module = __import__(name)
            module_dict[name] = module
            print(module)

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
