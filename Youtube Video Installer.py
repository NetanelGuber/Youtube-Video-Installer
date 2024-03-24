from pytube import YouTube
import os
from time import sleep

clear = lambda: os.system('cls' if os.name == 'nt' else 'clear')

def downloader():
    link = input("Enter the link to the video (URL): ")
    yt = YouTube(link)

    path = input("Where do you want the video to be downloaded to (path to folder)? ")

    print(f"Title: {yt.title}")
    print(f"Views: {yt.views}")

    yd = yt.streams.get_highest_resolution()
    yd.download(path)

    print("The video was downloaded.")
    sleep(3)
    clear()
    again()

def again():
    clear()
    playAgain = input("Would you like to download another video (y/n)? ").lower()

    if playAgain == "y":
        clear()
        downloader()
    elif playAgain == "n":
        exit()
    else:
        print("The options were y (yes) or n (no)")
        sleep(2)
        clear()
        again()

downloader()