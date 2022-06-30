# A space for tinkering with the tkinter GUI interface

import tkinter as tk
from tkinter import ttk

# Create the window
root = tk.Tk()
root.title("YouTube Playlist Downloader")
root.geometry("800x400")

pb = ttk.Progressbar(root, orient="horizontal", mode="indeterminate", length=280)
pb.pack()

start = ttk.Button(root, text="Start", command=pb.start).pack()
stop = ttk.Button(root, text="Stop", command=pb.stop).pack()

root.mainloop()
