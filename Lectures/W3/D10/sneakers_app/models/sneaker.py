from sneakers_app.models.user import User
from sneakers_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Sneaker:
    def __init__(self, data):
        self.id = data['id']
        self.brand = data['brand']
        self.size = data['size']
        self.type = data['type']
        self.price = data['price']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.user = None
    
    @staticmethod
    def validate_sneaker(data):
        is_valid = True
        if len(data['brand']) < 4:
            flash("Brand name must be at least 4 characters.", "brand")
            is_valid = False
        if int(data['price']) > 300:
            flash("Too expensive.", "price")
            is_valid = False
        
        return is_valid
    
    @classmethod
    def add_sneaker(cls, data):
        query = "INSERT INTO sneakers (brand, size, type, price, user_id) VALUES (%(brand)s, %(size)s, %(type)s, %(price)s, %(user_id)s);"

        new_sneaker_id = connectToMySQL('sneakers').query_db(query, data)
        return new_sneaker_id
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sneakers JOIN users ON user_id = users.id;"
        results = connectToMySQL('sneakers').query_db(query)

        all_sneakers = []

        for row in results:
            this_sneaker = cls(row)
            data = {
                'id' : row['users.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'email' : row['email'],
                'password' : row['password'],
                'created_at' : row['users.created_at'],
                'updated_at' : row['users.updated_at']
            }
            this_sneaker.user = User(data)
            all_sneakers.append(this_sneaker)
            
        return all_sneakers



