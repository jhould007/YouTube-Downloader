# File containing the main program flow
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from threading import Thread
import download

# Create the window
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("950x700")

# Set font style
normalFont = tk.font.nametofont("TkDefaultFont")
normalFont.config(size=14)

# Welcome messages
welcome = tk.Label(root, text="Welcome to the YouTube downloader!", foreground="#dd5454").pack()
instructions = tk.Label(root, text="Download your YouTube video or playlist by entering the URL in the text box below.").pack(pady=10)
warning = tk.Label(root, text="WARNING: There is currently no way to pause or cancel a download once started. \n Please make sure you really want to download the video or playlist (and are willing to wait) before starting! \n I am working on a fix for this.\n Also, you cannot download multiple things sequentially. \n After one download, please close the program and reopen it.").pack(pady=10)

# Input box to enter the playlist URL
URLbox = ttk.Entry(root, width=80)
URLbox.pack()

# Radio button allowing the user to specify audio or video
videoOrAudio = tk.Label(root, text="Do you want to download the video or playlist as video or audio? (Both are MP4 format)").pack(pady=10)
selected = tk.StringVar()
video = ttk.Radiobutton(root, text='Video', value="Video", variable=selected).pack()
audio = ttk.Radiobutton(root, text='Audio', value="Audio", variable=selected).pack()

def startThreads(): 
    downloadThread.start()       

# Gets input from the text boxes and starts the download  
def downloadFunc():  
    url = URLbox.get()
    if selected.get() == "Video": 
        if "watch" in url:
            download.downloadVideo(url, root)
        elif "playlist" in url:
            download.downloadPlaylist(url, root)
    elif selected.get() == "Audio":
        if "watch" in url: 
            download.downloadAudio(url, root)
        elif "playlist" in url:
            download.downloadPlaylistAudio(url, root)
    downloadMessage = tk.Label(root, text="✔️ Download finished!").pack()
    
# Create a button to submit
submit = ttk.Button(root, text="⬇ Download", command=startThreads).pack(pady=30)
downloadThread = Thread(target=downloadFunc)

# Disclaimer
disclaimer = tk.Label(root, text="⚠️ By using this tool, you agree to abide by all laws regarding copyrighted material.", justify="center", bg="red", fg="white").pack(pady=30)

root.mainloop()