from flask import render_template, redirect, session, request
from sneakers_app.models.user import User
from sneakers_app import app
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/users')
def users():
    all_users = User.all_users()
    return render_template('users.html', all_users = all_users)

@app.route('/add_user', methods=['post'])
def add_user():
    if not User.validate_user(request.form):
        return redirect('/users')

    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : pw_hash
    }

    User.create_user(data)
    return redirect('/users')

@app.route('/user/<id>')
def this_user(id):
    user = User.get_one({'id':id})
    return render_template('one_user.html', user = user)