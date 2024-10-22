from bson import ObjectId

class Product:
    def __init__(self, name, price, stock, category, _id=None):
        self.id = str(_id) if _id else None
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

    def to_dict(self):
        return {
            "_id": ObjectId(self.id) if self.id else None,
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "stock": self.stock
        }
