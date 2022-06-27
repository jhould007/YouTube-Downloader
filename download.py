from pytube import YouTube
from pytube import Playlist

# This is a simple python program I wrote using the pytube library to download YouTube playlists, since I was sick of trying various janky websites that never seemed to work properly.

# HOW TO USE
# 1) Write a function call in one of the formats shown below, depending on if you want the playlist as video or audio only.
# 2) Open a terminal window and type "python download.py" without the quotes.
# 3) The videos will start downloading into the root directory. Once the process is done, you can move them wherever you like.
# 4) Enjoy!

# Downloads a playlist as mp4 audio
def downloadPlaylistAudio(url):
    playlist = Playlist(url)
    for url in playlist.video_urls:
        video = YouTube(url)
        video.streams.get_audio_only().download()

# Downloads a playlist as mp4 video
def downloadPlaylist(url):
    playlist = Playlist(url)
    for url in playlist.video_urls:
        video = YouTube(url)
        video.streams.get_highest_resolution().download()


# How to download a playlist as mp4 audio
# downloadPlaylistAudio("url")

# How to download a playlist as mp4 video
# downloadPlaylist("url")
