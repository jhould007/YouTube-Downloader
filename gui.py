import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import download

#Create the window
root = tk.Tk()
root.title("YouTube Playlist Downloader")
root.geometry("800x400")

#Set font style
normalFont = tk.font.nametofont("TkDefaultFont")
normalFont.config(size=14)

# Welcome messages
welcome = tk.Label(root, text="Welcome to the YouTube playlist downloader!")
message1 = tk.Label(root, text="Download your YouTube playlist by entering the playlist URL in the first text box below.")
welcome.pack()
message1.pack(pady=10)

#Input box to enter the playlist URL
playlistURLbox = ttk.Entry(root, width=80)
playlistURLbox.pack()

#Radio button allowing the user to specify audio or video
message2 = tk.Label(root, text="Do you want to download the playlist as audio or video? (Both are MP4 format)")
message2.pack(pady=10)
selected = tk.StringVar()
video = ttk.Radiobutton(root, text='Video', value="Video", variable=selected)
audio = ttk.Radiobutton(root, text='Audio', value="Audio", variable=selected)
video.pack()
audio.pack()
  
#Gets input from the text boxes and starts the download  
def processInput(): 
    url = playlistURLbox.get()
    print(selected.get())
    if selected.get() == "Video": 
        download.downloadPlaylist(url)
    elif selected.get() == "Audio":
        download.downloadPlaylistAudio(url)
    downloadMessage = tk.Label(root, text="Downloading...")
    downloadMessage.pack(pady=30)

#Create a button to submit
submit = ttk.Button(root, text="⬇ Download", command=processInput)
submit.pack(pady=30)

root.mainloop()

#THINGS TO WORK ON NEXT: 
#1) Selecting download location
    # After location is specified, create a folder with the same name as the playlist and download videos to it
    
# Playlist for testing: A.L.I.S.O.N Signal Flow: https://www.youtube.com/playlist?list=PLacVPaaQL077XmlCCniHI9ikxa4FsDHpi

#Input box to enter the file path where the files should be saved
#message2 = tk.Label(root, text="Enter the file path where you want to save the downloaded files in the second text box below.")
#filePathBox = ttk.Entry(root, width=80)

#message2.pack(pady=10)
#filePathBox.pack()