import tkinter as tk
from app.views.product_management import ProductManagementUI

class Dashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Dashboard")

        tk.Button(self.root, text="Manage Products",
                  command=self.open_products).pack(pady=10)

        self.root.mainloop()

    def open_products(self):
        ProductManagementUI(self.root)
