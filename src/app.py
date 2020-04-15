from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/recipes/add')
def add():
    return render_template('add.html')

@app.route('/recipes')
def search():
    return render_template('search.html')

@app.route('/recipes/<id>')
def display(id):
    return render_template('view.html', id=id)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')