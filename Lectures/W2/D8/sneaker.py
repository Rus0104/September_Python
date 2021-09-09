from mysqlconnection import connectToMySQL

class Sneaker:
    def __init__(self, data):
        self.id = data['id']
        self.brand = data['brand']
        self.size = data['size']
        self.type = data['type']
        self.price = data['price']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def add_sneaker(cls, data):
        query = "INSERT INTO sneakers (brand, size, type, price) VALUES (%(brand)s, %(size)s, %(type)s, %(price)s);"

        new_sneaker_id = connectToMySQL('sneakers').query_db(query, data)
        return new_sneaker_id
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM sneakers;"
        results = connectToMySQL('sneakers').query_db(query)

        all_sneakers = []

        for row in results:
            all_sneakers.append(cls(row))
        
        return all_sneakers



