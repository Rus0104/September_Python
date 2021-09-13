from sneakers_app.config.mysqlconnection import connectToMySQL
from sneakers_app.models import sneaker
from flask import flash
import re

email_regex = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.sneakers = []

    @staticmethod
    def validate_user(data):
        is_valid = True

        if len(data['first_name']) < 2:
            flash('First name must be at least 2 characters.', 'first_name')
            is_valid = False
        if len(data['last_name']) < 2:
            flash('Last name must be at least 2 characters.', 'last_name')
            is_valid = False
        if not email_regex.match(data['email']):
            flash("Invalid email address.", 'email')
            is_valid = False
        if len(data['password']) < 8:
            flash('Password must be at least 8 characters.', 'password')
            is_valid = False
        
        return is_valid
        
        
    
    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        new_user_id = connectToMySQL('sneakers').query_db(query, data)
        return new_user_id
    
    @classmethod
    def all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('sneakers').query_db(query)

        users = []

        for row in results:
            users.append(cls(row))
        
        return users
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users LEFT JOIN sneakers ON users.id = sneakers.user_id WHERE users.id = %(id)s;"
        results = connectToMySQL('sneakers').query_db(query, data)

        user = cls(results[0])

        for row in results:
            data = {
                'id' : row['sneakers.id'],
                'brand' : row['brand'],
                'size' : row['size'],
                'type' : row['type'],
                'price' : row['price'],
                'created_at' : row['sneakers.created_at'],
                'updated_at' : row['sneakers.updated_at'],
                'user_id' : row['user_id']
            }
            user.sneakers.append(sneaker.Sneaker(data))
        
        return user
