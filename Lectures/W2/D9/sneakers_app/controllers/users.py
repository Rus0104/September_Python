from flask import render_template, redirect, session, request
from sneakers_app.models.user import User
from sneakers_app import app

@app.route('/users')
def users():
    all_users = User.all_users()
    return render_template('users.html', all_users = all_users)

@app.route('/add_user', methods=['post'])
def add_user():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name']
    }
    User.create_user(data)
    return redirect('/users')