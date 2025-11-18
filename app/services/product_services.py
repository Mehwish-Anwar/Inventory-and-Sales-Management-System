from app.models.db import db

class ProductService:

    @staticmethod
    def add_product(name, price, quantity):
        q = "INSERT INTO products (name, price, quantity) VALUES (%s, %s, %s)"
        db.execute(q, (name, price, quantity))

    @staticmethod
    def get_products():
        return db.execute("SELECT * FROM products").fetchall()

    @staticmethod
    def update_product(pid, name, price, qty):
        q = "UPDATE products SET name=%s, price=%s, quantity=%s WHERE id=%s"
        db.execute(q, (name, price, qty, pid))

    @staticmethod
    def delete_product(pid):
        db.execute("DELETE FROM products WHERE id=%s", (pid,))
