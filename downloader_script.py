
# ----------------------------------------------------------------
# Youtube Playlist Downloader
# version: v1.0
# Description: This is the Python based script to download
# youtube playlists on directories onto your system
# based on pytube python module
# pytube copyright reserved to its Respective Owner
# Script Created by Sanskar Pandey (aka zer0)
# ----------------------------------------------------------------

from pytube import Playlist
import os

print("[Python Playlist Downloader Script v1.0 - pytube]\n")

def rename(filename, i):
    newName = str(i) + ". " + str(filename)
    os.rename(filename, newName)

yt_playlist = Playlist(input("Playlist URL: "))
i = 0

dir = yt_playlist.title

try:
    os.mkdir(dir)

except:
    print(dir + " can't be created")
    dir = input("Write Custom Playlist Directory Name: ")

finally:
    for video in yt_playlist.videos:
        # try:
        video.streams.get_highest_resolution().download(dir)
        print(video.title, " Done!!")
        rename(video.title, i+1)
            
        # except:
        #     print(video.title + " video can't be downloaded")

print("\nPlaylist Downloaded Successfully.")
