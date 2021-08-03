import tkinter
import urllib
from pytube import YouTube
 
root = tkinter.Tk()
root.geometry('500x300')
root.configure(bg='black')
root.resizable(0,0)
root.title("IT SOURCECODE Youtube Video Downloader")
 

tkinter.Label(root, text ='YOUTUBE VIDEO DOWNLOADER BY H-CORE', font ='Helvetica 15 bold underline', bg='#00ffff').pack()
 
link = tkinter.StringVar()
 
tkinter.Label(root, text ='Paste Link Here:', font ='arial 15 bold').place(x= 160, y = 60)
link_enter = tkinter.Entry(root, width = 70, textvariable = link).place(x = 32, y = 90)
 
 
def download():
    
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    tkinter.Label(root, text ='DOWNLOADED', font ='arial 15').place(x= 180, y = 210)
 
 
tkinter.Button(root, text ='Download', font ='arial 12 bold', bg ='#00FFFF', padx = 3, command = download).place(x=180, y = 150)
 
 
 
root.mainloop()