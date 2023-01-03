import pytube
from moviepy.editor import VideoFileClip
import os
import time
from PIL import Image, ImageTk
from tkinter import *
# from tkinter.ttk import *

from moviepy.audio.fx.audio_fadein import audio_fadein
from moviepy.audio.fx.audio_fadeout import audio_fadeout
from moviepy.audio.fx.audio_left_right import audio_left_right
from moviepy.audio.fx.audio_loop import audio_loop
from moviepy.audio.fx.audio_normalize import audio_normalize
from moviepy.audio.fx.volumex import volumex

from moviepy.video.fx.accel_decel import accel_decel
from moviepy.video.fx.blackwhite import blackwhite
from moviepy.video.fx.blink import blink
from moviepy.video.fx.colorx import colorx
from moviepy.video.fx.crop import crop
from moviepy.video.fx.even_size import even_size
from moviepy.video.fx.fadein import fadein
from moviepy.video.fx.fadeout import fadeout
from moviepy.video.fx.freeze import freeze
from moviepy.video.fx.freeze_region import freeze_region
from moviepy.video.fx.gamma_corr import gamma_corr
from moviepy.video.fx.headblur import headblur
from moviepy.video.fx.invert_colors import invert_colors
from moviepy.video.fx.loop import loop
from moviepy.video.fx.lum_contrast import lum_contrast
from moviepy.video.fx.make_loopable import make_loopable
from moviepy.video.fx.margin import margin
from moviepy.video.fx.mask_and import mask_and
from moviepy.video.fx.mask_color import mask_color
from moviepy.video.fx.mask_or import mask_or
from moviepy.video.fx.mirror_x import mirror_x
from moviepy.video.fx.mirror_y import mirror_y
from moviepy.video.fx.painting import painting
from moviepy.video.fx.resize import resize
from moviepy.video.fx.rotate import rotate
from moviepy.video.fx.scroll import scroll
from moviepy.video.fx.speedx import speedx
from moviepy.video.fx.supersample import supersample
from moviepy.video.fx.time_mirror import time_mirror
from moviepy.video.fx.time_symmetrize import time_symmetrize

# print("Welcome to YouTube Downloader and Converter")
# print("Loading...")

location="Downloads"
choice=0

def close():
    root.quit()

def convert_to_mp3(filename):
    for widgets in frame.winfo_children():
        widgets.destroy()
    root.geometry("500x220")
    root.title("✅Converting....⏱️")   
    # p2 = PhotoImage('./checked.png')
    # root.iconphoto(False, p2) 
    mylable=Label(frame,text="\nConverted Sucessfully😊\n",font=("Calibri", 25))
    mylable.pack()
    mybutton=Button(frame,text="Close",padx=20,pady=5,command=close)
    mybutton.pack(anchor="center")
    
    global location
    clip = VideoFileClip("./"+location+"/"+filename)
    clip.audio.write_audiofile("./"+location+"/"+ filename[:-4] + ".mp3")
    clip.close()

def download_video(url, resolution):
    for widgets in frame.winfo_children():
        widgets.destroy()
    root.geometry("500x220")
    root.title("✅Downloading...⏱️")  
    
    # p2 = PhotoImage('checked.png')
    # root.iconphoto(False, p2) 
    
    # ico = Image.open('test.jpg')
    # photo = ImageTk.PhotoImage(ico)
    # root.wm_iconphoto(False, photo)
    
    mylable=Label(frame,text="\nDownload Completed😊\n",font=("Calibri", 25))
    mylable.pack()
    mybutton=Button(frame,text="Close",padx=20,pady=5,command=close)
    mybutton.pack(anchor="center")
    # time.sleep(1)
    global location
    if not os.path.exists(location):
        os.mkdir(location)
    itag = choose_resolution(resolution)
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(itag)
    stream.download("./"+location)
    # print(stream.default_filename)
    return stream.default_filename

def download_videos(urls, resolution):
    for url in urls:
        download_video(url, resolution)

def download_playlist(url, resolution):
    playlist = pytube.Playlist(url)
    global location
    location="playlist"
    download_videos(playlist.video_urls, resolution)

def choose_resolution(resolution):
    if resolution =="1":
        itag = 18
    elif resolution =="2":
        itag = 22
    elif resolution =="3":
        itag = 137
    elif resolution =="4":
        itag = 313
    else:
        itag = 22
    return itag


root = Tk()
root.geometry("550x350")
root.title("Welcome")
# p1 = PhotoImage('E:\Codes\youtube100.png')
# root.iconphoto(False, p1)
# root=BitmapImage('E:\Codes\youtube100.ico') 
w = Label(root, text ='', font = "50")
w.pack()

frame = Frame(root)
frame.pack(side= TOP)
 
v = StringVar(frame,"1")

mylable=Label(frame,text="YouTube Downloader and Converter\n",font=("Calibri", 25))
mylable.pack()
mylable1=Label(frame,text="What do you want?\n",font=("Arial", 12))
mylable1.pack(anchor="w",ipadx=5)
# print(frame) 

# Dictionary to create multiple buttons
values = {"Download YouTube Videos Manually" : "1",
        "Download a YouTube Playlist" : "2",
        "Download YouTube Videos and Convert Into MP3" : "3",}
 
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(frame, text = text, variable = v,
        value = value).pack(side = TOP, ipady = 5,anchor="w" ,ipadx= 30)
    
def btn():
    global choice,frame,v
    choice=v.get()
    for widgets in frame.winfo_children():
        widgets.destroy()
    
    root.title("Quality")
    mylable1=Label(frame,text="Please choose a quality:\n\n",font=("Arial", 15))
    mylable1.pack(anchor="w",ipadx=5)
    v = StringVar(frame,"1")
    values = {"360p [Low]" : "1",
    "720p [HD]" : "2",
    "1080p [Full HD]" : "3",
    "2160p [4K]" : "4"}
    for (text, value) in values.items():
        Radiobutton(frame, text = text, variable = v,
        value = value).pack(side = TOP, ipady = 5,anchor="w" ,ipadx= 30)
    mylable2=Label(frame,text="\n\n")
    mylable2.pack(anchor="w")
    mybutton=Button(frame,text="Next",padx=20,pady=5,command=button_qty)
    mybutton.pack(anchor="center")
    
def button_qty():
    global v
    quality=v.get()
    link=Entry(frame,width=80)
    for widgets in frame.winfo_children():
        widgets.destroy()
    run(choice,frame,quality,link)
        
mylable2=Label(frame,text="\n")
mylable2.pack(anchor="w") 
mybutton=Button(frame,text="Next",padx=20,pady=5,command=btn)
mybutton.pack(anchor="center")
mylable3=Label(frame,text="\n")
mylable3.pack(anchor="w") 
# root.protocol('WM_DELETE_WINDOW',btn)
    

def run(choice,frame,quality,link):
        
    def lk1():
        download_video(link.get(), quality)
        
    def lk2():
        download_playlist(link.get(), quality)
        
    def lk3():
        a=link.get()
        # for widgets in frame.winfo_children():
        #     widgets.destroy()
        # root.geometry("500x100")
        # root.title("Downloading....")   
        # mylable=Label(frame,text="\nConverting...\n",font=("Calibri", 25))
        # mylable.pack()
        # time.sleep(1)
        filename = download_video(a, '1')
        convert_to_mp3(filename)

    if choice == "1":
        root.title("Video's Link")
        root.geometry("550x240")
        mylable1=Label(frame,text="\nEnter Link of video:\n",font=("Arial", 15))
        mylable1.pack(anchor="w",ipadx=5)
        link=Entry(frame,width=80)
        link.pack()
        mylable2=Label(frame,text='\n\n')
        mylable2.pack()
        
        mybutton=Button(frame,text="Submit",padx=22,pady=5,command=lk1)
        mybutton.pack(anchor="center")
            
            
    elif choice == "2":
        root.title("Playlist's Link")
        root.geometry("550x240")
        mylable1=Label(frame,text="\nEnter Link of playlist:\n",font=("Arial", 15))
        mylable1.pack(anchor="w",ipadx=5)
        link=Entry(frame,width=80)
        link.pack()
        mylable2=Label(frame,text='\n\n')
        mylable2.pack()
        mybutton=Button(frame,text="Submit",padx=22,pady=5,command=lk2)
        mybutton.pack(anchor="center")
        
        
    elif choice == "3":
        root.title("Mp3 Convertor")
        root.geometry("550x240")
        mylable1=Label(frame,text="\nEnter Link of video:\n",font=("Arial", 15))
        mylable1.pack(anchor="w",ipadx=5)
        link=Entry(frame,width=80)
        link.pack()
        mylable2=Label(frame,text='\n\n')
        mylable2.pack()
        mybutton=Button(frame,text="Submit",padx=22,pady=5,command=lk3)
        mybutton.pack(anchor="center")
        
root.mainloop()