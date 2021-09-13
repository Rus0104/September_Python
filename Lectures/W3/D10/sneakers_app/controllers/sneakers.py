from flask import render_template, redirect, session, request
from sneakers_app.models.sneaker import Sneaker
from sneakers_app.models.user import User
from sneakers_app import app

@app.route('/')
def index():
    all_users = User.all_users()
    return render_template('index.html', all_users = all_users)

@app.route('/add_sneakers', methods=['post'])
def add_sneaker():
    data = {
        'brand' : request.form['brand'],
        'type' : request.form['type'],
        'size' : request.form['size'],
        'price' : request.form['price'],
        'user_id' : request.form['user_id']
    }

    if not Sneaker.validate_sneaker(request.form):
        return redirect('/')

    new_sneaker_id = Sneaker.add_sneaker(request.form)

    return redirect('/all_sneakers')

@app.route('/all_sneakers')
def all_sneakers():
    all_sneakers = Sneaker.get_all()
    return render_template('sneakers.html', all_sneakers = all_sneakers)