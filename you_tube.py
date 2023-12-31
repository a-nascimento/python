# to use this program first you need to install pytube
# in the terminal:
#
# pip install pytube
#


from pytube import YouTube
import sys

videoURL = ""
if len(sys.argv) > 1:
    videoURL = sys.argv[1]
if "youtube.com" not in videoURL:
    videoURL = input("Enter YouTube URL: ")
yt = YouTube(videoURL, use_oauth=True, allow_oauth_cache=True)
filename = yt.title.replace(" ", "_")
print("Downloading YouTube File: " + yt.title)
yt.streams.first().download(filename=filename + ".mp4")
