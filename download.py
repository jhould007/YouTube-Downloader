from pytube import YouTube
from pytube import Playlist

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
