from flask import Flask, render_template, request, redirect, url_for, Response
from fileManagement.directory import fileBlueprint
from projectManagement.directory import projectBlueprint
import xml.etree.ElementTree as ET

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

app.register_blueprint(fileBlueprint)
app.register_blueprint(projectBlueprint)

if __name__ == '__main__':
    app.run(debug=True)