import tkinter as tk
from tkinter import ttk, messagebox
from app.services.product_service import ProductService

class ProductManagementUI:

    def __init__(self, parent):
        self.win = tk.Toplevel(parent)
        self.win.title("Product Management")

        tk.Label(self.win, text="Name:").grid(row=0, column=0)
        tk.Label(self.win, text="Price:").grid(row=1, column=0)
        tk.Label(self.win, text="Qty:").grid(row=2, column=0)

        self.name = tk.Entry(self.win)
        self.price = tk.Entry(self.win)
        self.qty = tk.Entry(self.win)

        self.name.grid(row=0, column=1)
        self.price.grid(row=1, column=1)
        self.qty.grid(row=2, column=1)

        tk.Button(self.win, text="Add", command=self.add_product).grid(row=3, column=0)
        tk.Button(self.win, text="Update", command=self.update_product).grid(row=3, column=1)
        tk.Button(self.win, text="Delete", command=self.delete_product).grid(row=3, column=2)

        self.table = ttk.Treeview(self.win, columns=("id", "name", "price", "qty"))
        self.table.heading("id", text="ID")
        self.table.heading("name", text="Name")
        self.table.heading("price", text="Price")
        self.table.heading("qty", text="Qty")
        self.table.grid(row=4, column=0, columnspan=3)

        self.table.bind("<ButtonRelease-1>", self.select_row)
        self.load()

    def load(self):
        for row in self.table.get_children():
            self.table.delete(row)
        for p in ProductService.get_products():
            self.table.insert("", "end", values=(p["id"], p["name"], p["price"], p["quantity"]))

    def select_row(self, event):
        item = self.table.item(self.table.focus())["values"]
        self.id = item[0]
        self.name.delete(0, tk.END)
        self.name.insert(0, item[1])
        self.price.delete(0, tk.END)
        self.price.insert(0, item[2])
        self.qty.delete(0, tk.END)
        self.qty.insert(0, item[3])

    def add_product(self):
        ProductService.add_product(self.name.get(), self.price.get(), self.qty.get())
        self.load()

    def update_product(self):
        ProductService.update_product(self.id, self.name.get(), self.price.get(), self.qty.get())
        self.load()

    def delete_product(self):
        ProductService.delete_product(self.id)
        self.load()
