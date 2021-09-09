from flask import render_template, redirect, request, session
from burger_app import app

@app.route('/users')
def users():
    return "THIS IS THE ROUTE FROM THE USER'S CONTROLLER"