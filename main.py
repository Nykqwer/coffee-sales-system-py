import tkinter as tk
from build.login_frame.gui5 import loginPage

# Main window constructor
root = tk.Tk()  # Make temporary window for app to start
root.withdraw()  # WithDraw the window


if __name__ == "__main__":

    loginPage()
    #mainWindow()

    root.mainloop()
