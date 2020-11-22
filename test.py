import sys
import ssl
import urllib.request
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from pytube import YouTube

Folder_name =" "

#choosing a path directory for user
def openLocation():
    global Folder_name
    Folder_name = filedialog.askdirectory()
    if(len(Folder_name)> 1):
        locationError.config(text=Folder_name,fg="green")

    else:
        locationError.config(text="Please choose folder!",fg="red")

#download the video
def DownloadVideo():
    choice = ytdChoices.get()
    url = ytdEntry.get()

    if(len(url)>1):
        ytdError.config(text="")
        yt = YouTube(url)
        #Resolution choices: "720p", "144p","Only Audio"

        if(choice == choices[0]): #720
            select = yt.streams.filter(progressive=True).first()
        
        elif(choice == choices[1]): #144p
            select = yt.streams.filter(progressive=True,file_extension='mp4').last()

        elif(choice == choices[2]): #audio only
            select = yt.streams.filter(only_audio=True).first()

        else:
            ytdError.config(Text="Paste link again!",fg="red")

    #download function
    select.download(Folder_name)
    ytdError.config(text="Download complete!")


#Python GUI tkinter code
root = Tk()
root.title('YouTube Downloader')
root.geometry("500x500")#set window
root.columnconfigure(0,weight=1)#set all content in center

#Youtube Downloader name label
theLabel =  Label(root,text="Enter the URL of the video",font=("Arial",24,"bold"))
theLabel.grid()


#user entry box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=50,textvariable=ytdEntryVar)
ytdEntry.grid()

#error msg
ytdError = Label(root,text="Error Message",fg="red",font=("Arial",16))
ytdError.grid()

#asking save file label
saveLabel = Label(root,text="Save the video file",font=("Arial",24,"bold"))
saveLabel.grid()

#button for save file
saveEntry = Button(root,width=10,highlightbackground="#FF4141",fg="white",text="Choose folder",command=openLocation)
saveEntry.grid()

#error msg location
locationError = Label(root,text="Error message of path",fg="red",font=("Arial",16))
locationError.grid()

#Download quality
ytQuality = Label(root,text="Select quality",font=("Arial",22))
ytQuality.grid()

#video quality choices drop down list
choices = ["720p","144p","Only Audio"]
ytdChoices = ttk.Combobox(root,values=choices)
ytdChoices.grid()

#download button
downloadBtn = Button(root,text="Download",width=10,highlightbackground="#FF4141",fg="white",command=DownloadVideo)
downloadBtn.grid()

#developer label, ME AND MYSELF
developerLabel = Label(root,text="Developed by Bill Liza",font=("Arial",24))
developerLabel.grid()


root.mainloop()
