import os
from tkinter.filedialog import askdirectory,askopenfilename
 
import pygame
from mutagen.id3 import ID3
from tkinter import *
 
root = Tk()
root.minsize(300,300)
 
 
listofsongs = []
realnames = []
v = StringVar()
songlabel = Label(root,textvariable=v,width=100)
 
index = 0
 
def directorychooser():
 
    directory = askdirectory()
    os.chdir(directory)
 
    for files in os.listdir(directory):
        if files.endswith(".mp3"):
 
            realdir = os.path.realpath(files)
            audio = ID3(realdir)
            realnames.append(files)
            
 
 
            listofsongs.append(files)
            

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    #pygame.mixer.music.play()




 
directorychooser()
 
def updatelabel():
    global index
    v.set(realnames[index])
 
 
 
def nextsong(event):
    global index
    if(index<len(realnames)-1):
        index += 1
    else:
       index = 0
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
 
def prevsong(event):
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()
 
def playsong(event):
    pygame.mixer.music.play()
    updatelabel()


def stopsong(event):
    pygame.mixer.music.stop()
    v.set("")
    updatelabel()

def pausesong(event):
    pygame.mixer.music.pause()
    updatelabel()
    

 
 
label = Label(root,text='Music Player')
label.pack()
 
listbox = Listbox(root)
listbox.pack()
 
#listofsongs.reverse()
realnames.reverse()
 
for items in realnames:
    listbox.insert(0,items)
 
realnames.reverse()
#listofsongs.reverse()
 
 
nextbutton = Button(root,text = 'Next Song')
nextbutton.pack()
 
previousbutton = Button(root,text = 'Previous Song')
previousbutton.pack()
 
stopbutton = Button(root,text='Stop Music')
stopbutton.pack()
 
playbutton = Button(root,text='play music')
playbutton.pack()

pausebutton = Button(root,text='pause music')
pausebutton.pack()


nextbutton.bind("<Button-1>",nextsong)
previousbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)
playbutton.bind("<Button-1>",playsong)
pausebutton.bind("<Button-1>",pausesong)

songlabel.pack()
 
root.mainloop()
