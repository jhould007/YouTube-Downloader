# File containing the main program flow
import time
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from threading import Thread
import download

# Create the window
root = tk.Tk()
root.title("YouTube Playlist Downloader")
root.geometry("800x500")

# Set font style
normalFont = tk.font.nametofont("TkDefaultFont")
normalFont.config(size=14)

# Welcome messages
welcome = tk.Label(root, text="Welcome to the YouTube playlist downloader!", foreground="#dd5454").pack()
message1 = tk.Label(root, text="Download your YouTube playlist by entering the playlist URL in the text box below.").pack(pady=10)

# Input box to enter the playlist URL
playlistURLbox = ttk.Entry(root, width=80)
playlistURLbox.pack()

# Radio button allowing the user to specify audio or video
message2 = tk.Label(root, text="Do you want to download the playlist as video or audio? (Both are MP4 format)").pack(pady=10)
selected = tk.StringVar()
video = ttk.Radiobutton(root, text='Video', value="Video", variable=selected).pack()
audio = ttk.Radiobutton(root, text='Audio', value="Audio", variable=selected).pack()

def startThread(): 
    t.start()
  
# Gets input from the text boxes and starts the download  
def processInput(): 
    url = playlistURLbox.get()
    if selected.get() == "Video": 
        download.downloadPlaylist(url)
    elif selected.get() == "Audio":
        download.downloadPlaylistAudio(url)
    downloadMessage = tk.Label(root, text="Download finished!").pack(pady=30)
    
# Create a button to submit
submit = ttk.Button(root, text="⬇ Download", command=startThread).pack(pady=30)

t = Thread(target=processInput)

# Disclaimer
disclaimer = tk.Label(root, text="⚠️ By using this tool, you agree to abide by all laws regarding copyrighted material.", justify="center", bg="red", fg="white").pack(pady=30)

root.mainloop()
    
# Playlist for testing: A.L.I.S.O.N Signal Flow: https://www.youtube.com/playlist?list=PLacVPaaQL077XmlCCniHI9ikxa4FsDHpi