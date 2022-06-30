# A file containing the functions responsible for downloading the playlist
from pytube import YouTube
from pytube import Playlist
import os
from pathlib import Path
import helper

downloadPath = str(os.path.join(Path.home(), "Downloads"))

# Downloads a playlist as mp4 video
def downloadPlaylist(url):
    playlist = Playlist(url)
    folderName = helper.cleanString(playlist.title)
    helper.deleteFolder(folderName)
    path = helper.createFolder(folderName)
    for url in playlist.video_urls:
        video = YouTube(url)
        video.streams.get_highest_resolution().download(path)

# Downloads a playlist as mp4 audio
def downloadPlaylistAudio(url):
    playlist = Playlist(url)
    folderName = helper.cleanString(playlist.title)
    helper.deleteFolder(folderName)
    path = helper.createFolder(folderName)
    for url in playlist.video_urls:
        video = YouTube(url)
        video.title = helper.cleanString(video.title)
        video.streams.get_audio_only().download(path)

# Returns the number of videos in a playlist
def countVideos(url): 
    playlist = Playlist(url)
    videoCount = 0
    for url in playlist.video_urls: 
        videoCount += 1
    print("There are " + str(videoCount) + " videos in this playlist.")
    return videoCount