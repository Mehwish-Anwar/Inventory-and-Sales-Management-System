import tkinter as tk
from app.views.login import LoginUI

if __name__ == "__main__":
    root = tk.Tk()
    LoginUI(root)
    root.mainloop()
