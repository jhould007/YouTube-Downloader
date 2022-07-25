# A file containing the functions responsible for downloading the playlist
from time import sleep
from pytube import YouTube
from pytube import Playlist
import os
from pathlib import Path
import helper
import tkinter as tk
from tkinter import StringVar, ttk
import tkinter.font as tkFont

downloadPath = str(os.path.join(Path.home(), "Downloads"))

#Downloads a video as mp4 video
def downloadVideo(url, root):
    video = YouTube(url)
    video.title = helper.cleanString(video.title)
    downloadedText = StringVar()
    downloadedText.set("")
    downloadedLabel = ttk.Label(root, textvariable=downloadedText).pack(pady=10)
    video.streams.get_highest_resolution().download(downloadPath)
    downloadedText.set("Downloaded video. Title of video: \"" + video.title + "\"")
    print("Download complete!")

#Downloads a video as mp4 audio
def downloadAudio(url, root):
    video = YouTube(url)
    video.title = helper.cleanString(video.title)
    downloadedText = StringVar()
    downloadedText.set("")
    downloadedLabel = ttk.Label(root, textvariable=downloadedText).pack(pady=10)
    video.streams.get_audio_only().download(downloadPath)
    downloadedText.set("Downloaded video. Title of video: \"" + video.title + "\"")
    print("Download complete!")

# Downloads a playlist as mp4 video
def downloadPlaylist(url, root):
    playlist = Playlist(url)
    videoCount = len(playlist.video_urls)
    videoIndex = 1
    folderName = helper.cleanString(playlist.title)
    helper.deleteFolder(folderName)
    path = helper.createFolder(folderName)
    downloadedText = StringVar()
    downloadedText.set("")
    downloadedLabel = ttk.Label(root, textvariable=downloadedText).pack(pady=10)
    for url in playlist.video_urls:
        video = YouTube(url)
        video.title = helper.cleanString(video.title)
        video.streams.get_highest_resolution().download(path) #I think this line might be causing the issue
        downloadedText.set("Downloaded audio " + str(videoIndex) + " out of " + str(videoCount) + ". Title of video: \"" + video.title + "\"")
        print("Downloaded video " + str(videoIndex) + " out of " + str(videoCount) + ". Title of video: " + video.title)
        videoIndex += 1
    sleep(1)
    print("Download complete!")

# Downloads a playlist as mp4 audio
def downloadPlaylistAudio(url, root):
    playlist = Playlist(url)
    videoCount = len(playlist.video_urls)
    videoIndex = 1
    folderName = helper.cleanString(playlist.title)
    helper.deleteFolder(folderName)
    path = helper.createFolder(folderName)
    downloadedText = StringVar()
    downloadedText.set("")
    downloadedLabel = ttk.Label(root, textvariable=downloadedText).pack(pady=10)
    for url in playlist.video_urls:
        video = YouTube(url)
        video.title = helper.cleanString(video.title)
        video.streams.get_audio_only().download(path) 
        downloadedText.set("Downloaded audio " + str(videoIndex) + " out of " + str(videoCount) + ". Title of video: \"" + video.title + "\"")
        print("Downloaded audio " + str(videoIndex) + " out of " + str(videoCount) + ". Title of video: " + video.title)
        videoIndex += 1
    sleep(1)
    print("Download finished!")

# Returns the number of videos in a playlist
def countVideos(url): 
    playlist = Playlist(url)
    videoCount = 0
    for url in playlist.video_urls: 
        print("Video " + str(videoCount + 1) + ": " + url)
        videoCount += 1
    print("There are " + str(videoCount) + " videos in this playlist.")
    return videoCount

# How It's Actually Made: https://www.youtube.com/watch?v=-3v4OsPmsUg&list=PL845lQkWyS9JQRYTfFzhQSh1LbV75t20T

