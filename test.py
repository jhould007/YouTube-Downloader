from pytube import YouTube

def downloadVideo(url): 
    video = YouTube(url)
    video.streams.get_highest_resolution().download()
    
downloadVideo("https://www.youtube.com/watch?v=xSx-v1Jm2G8&t=2271")