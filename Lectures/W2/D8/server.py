from flask import Flask, render_template, request, redirect
from sneaker import Sneaker
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_sneakers', methods=['post'])
def add_sneaker():
    data = {
        'brand' : request.form['brand'],
        'type' : request.form['type'],
        'size' : request.form['size'],
        'price' : request.form['price'],
    }

    new_sneaker_id = Sneaker.add_sneaker(data)

    return redirect('/all_sneakers')

@app.route('/all_sneakers')
def all_sneakers():
    all_sneakers = Sneaker.get_all()
    return render_template('sneakers.html', all_sneakers = all_sneakers)


if __name__ == '__main__':
    app.run(debug=True)