# Import Modules
from tkinter import *
from tkinter.font import BOLD
import pygame
import os
from tkinter.filedialog import  askdirectory
from PIL import Image, ImageTk

# Creating TK Container
root = Tk()
root.title("Music Player")
root.geometry("815x500")
root.resizable(FALSE, FALSE)
root.config(background="black")
 # Initiating Pygame
pygame.init()
    # Initiating Pygame Mixer
pygame.mixer.init()
    
def Prevsong():
    next_one=playlist.curselection()
    next_one=next_one[0]-1
    song=playlist.get(next_one)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    #clear activee bar in playlist 
    playlist.selection_clear(0,END)
    #active new song bar
    playlist.activate(next_one)
    playlist.selection_set(next_one,last=None)
def playsong():
    # Displaying Selected Song title
    tr.set(playlist.get(ACTIVE))
    # Displaying Status
    status.set("-Playing")
    # Loading Selected Song
    pygame.mixer.music.load(playlist.get(ACTIVE))
    # Playing Selected Song
    pygame.mixer.music.play()
def Nextsong():
    next_one=playlist.curselection()
    next_one=next_one[0]+1
    song=playlist.get(next_one)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()
    #clear activee bar in playlist 
    playlist.selection_clear(0,END)
    #active new song bar
    playlist.activate(next_one)
    playlist.selection_set(next_one,last=None)
def pausesong():
    # Displaying Status
    status.set("-Paused")
    # Paused Song
    pygame.mixer.music.pause()

# Declaring Variable
tr = StringVar()
status = StringVar()

title=Frame(root, background="white",).pack()
titlelabel= Label(title,text="Music Player GUI Project",font=("arial",10 ,BOLD),background="gray22" ,fg="white").pack(fill=X)



songframe = Frame(root).place(x=20,y=5)
op = Image.open("unknown.png")
re= op.resize((120,120))
ren = ImageTk.PhotoImage(re)
songimage=Label(songframe,image=ren,borderwidth=0).place(x=20,y=50)
songname=Label(songframe,textvariable=tr,borderwidth=0,font=("arial",28,BOLD),bg="black",fg="white").place(x=160,y=50,width=600)

load1 = Image.open("back.png")
resize_image1 = load1.resize((30,30))
render1 = ImageTk.PhotoImage(resize_image1)

load2 = Image.open("play.png")
resize_image2 = load2.resize((30,30))
render2 = ImageTk.PhotoImage(resize_image2)

load3 = Image.open("next.png")
resize_image3 = load3.resize((30,30))
render3 = ImageTk.PhotoImage(resize_image3)

load4 = Image.open("stop.png")
resize_image4 = load4.resize((30,30))
render4 = ImageTk.PhotoImage(resize_image4)

songsframe = Frame(root, borderwidth=0,relief=FLAT, bd=0)
songsframe.place(x=20,y=250,width=780)
scrol_y = Scrollbar(songsframe, orient=VERTICAL)
playlist = Listbox(songsframe, yscrollcommand=scrol_y.set, selectbackground="gray10", selectmode=SINGLE, font=(
    "Regular 400",14, ), bg="black", fg="white", bd=0)
scrol_y.pack(side=RIGHT, fill=Y)
scrol_y.config(command=playlist.yview, orient="vertical", bg="light steel blue", troughcolor="steel blue", highlightcolor="light steel blue", activebackground="light steel blue", highlightbackground="light steel blue")
playlist.pack(fill=BOTH)

buttonframe = Frame(root,bd=5,).place(x=400,y=400)
Prev=Button(buttonframe,text="Prev",image=render1,command=Prevsong,bg="black" ,borderwidth=0).place(x=300,y=200)
play=Button(buttonframe,text="play",image=render2,command=playsong ,bg="black",borderwidth=0).place(x=400,y=200)
Next=Button(buttonframe,text="Next",image=render3,command=Nextsong,bg="black",borderwidth=0).place(x=500,y=200)
pause=Button(buttonframe,text="Pause",image=render4,command=pausesong,bg="white",borderwidth=0).place(x=600,y=200)

# Fetching Songs
directory = askdirectory()
os.chdir(directory)
songtracks = os.listdir()
# Inserting Songs into Playlist
for track in songtracks:
    playlist.insert(END, track)

# Root Window Looping
root.mainloop()
