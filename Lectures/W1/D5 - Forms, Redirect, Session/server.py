from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = "secretkeyyyyyyyy"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods = ['Post'])
def submit():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['favorite_dog'] = request.form['favorite_dog']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template('results.html', first_name = session['first_name'], last_name = session['last_name'], fav_dog = session['favorite_dog'])

if __name__ == "__main__":
    app.run(debug=True)