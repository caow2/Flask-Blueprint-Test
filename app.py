from flask import Flask
import os
import glob

path = './files/'
os.chdir(path)

filenames = []
for file in glob.glob('*.py'):
    name = file[:-3] #excludes .py
    filenames.append(name)
    #import name

print(filenames)
