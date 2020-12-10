#===========================
# Imports
#===========================
import tkinter as tk
from tkinter import ttk, colorchooser as cc, Menu, Spinbox as sb, scrolledtext as st, messagebox as mb, filedialog as fd, simpledialog as sd

import socket

#===========================
# Main App
#===========================
class App(tk.Tk):
    """Main Application."""
    #------------------------------------------
    # Initializer
    #------------------------------------------
    def __init__(self):
        super().__init__()
        self.init_config()
        self.init_vars()
        self.init_widgets()

    #-------------------------------------------
    # Window Settings
    #-------------------------------------------
    def init_config(self):
        self.resizable(True, True)
        self.title('Port Scanner Version 1.0')
        self.iconbitmap('python.ico')
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

    #------------------------------------------
    # Instance Variables
    #------------------------------------------
    def init_vars(self):
        self.ip = socket.gethostbyname(socket.gethostname()) # your ip address

    #-------------------------------------------
    # Widgets / Components
    #-------------------------------------------
    def init_widgets(self):
        frame = ttk.Frame(self)
        frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        textarea = st.ScrolledText(frame, width=50, height=20, wrap=tk.WORD)

        for port in range(65535): # all ports are in 0-65535
            try:
                serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create new socket
                serv.bind(self.ip, port) # bind port with your ip address
            except:
                textarea.insert(tk.END, f'[OPEN] port: {port}\n')
            serv.close()
        textarea.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


#===========================
# Start GUI
#===========================
def main():
    app = App()
    app.mainloop()

if __name__ == '__main__':
    main()
