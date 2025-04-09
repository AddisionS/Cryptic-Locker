import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("CrypticLocker")

        # Start maximized
        self.state('zoomed')

        # Set minimum window size (width x height)
        self.minsize(800, 300)

        tk.Label(self, text="Welcome to CrypticLocker", font=("Arial", 24)).pack(pady=100)

if __name__ == "__main__":
    app = App()
    app.mainloop()
