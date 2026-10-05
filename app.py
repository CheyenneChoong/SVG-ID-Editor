from flask import Flask, render_template
from fileManagement.directory import fileBlueprint
from projectManagement.directory import projectBlueprint

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

app.register_blueprint(fileBlueprint)
app.register_blueprint(projectBlueprint)

if __name__ == '__main__':
    app.run(debug=True)