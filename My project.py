# Importing libraries

from tkinter import * 
from pytube import YouTube

# Creating display window

root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title("YouTube Video Downloader")

Label(root, text='YouTube Video Downloader', font='arial 20 bold').place(x=70, y=30)

# Creating field to Enter link

link = StringVar()

Label(root, text='Paste Link Here:', font='arial 15 bold').place(x=170, y=100)
link_enter = Entry(root, width=70, textvariable=link).place(x=35, y=140)

# Create Function to Start Downloading

def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='DOWNLOADED', font='arial 15').place(x=180, y=210)

Button(root, text='DOWNLOAD', font='arial 15 bold', bg='#7AC5CD', padx=2, command=Downloader).place(x=180, y=180)

root.mainloop()