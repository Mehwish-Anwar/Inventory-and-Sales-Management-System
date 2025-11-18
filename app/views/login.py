import tkinter as tk
from tkinter import messagebox
from app.services.auth import AuthService
from app.views.dashboard import Dashboard

class LoginUI:

    def __init__(self, root):
        self.root = root
        root.title("Login")

        tk.Label(root, text="Username").pack()
        self.username = tk.Entry(root)
        self.username.pack()

        tk.Label(root, text="Password").pack()
        self.password = tk.Entry(root, show="*")
        self.password.pack()

        tk.Button(root, text="Login", command=self.login).pack()

    def login(self):
        user = AuthService.authenticate(
            self.username.get(),
            self.password.get()
        )

        if user:
            self.root.destroy()
            Dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials")
