# Python program to open the
# camera in Tkinter
# Import the libraries,
# tkinter, cv2, Image and ImageTk
  
from tkinter import *
import cv2
from PIL import Image, ImageTk
from subprocess import Popen
import os
import datetime as dt
import time
  
# Define a video capture object
vid = cv2.VideoCapture(0)
  
# Declare the width and height in variables
width, height = 800, 500
  
# Set the width and height
vid.set(cv2.CAP_PROP_FRAME_WIDTH, width)
vid.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
  
# Create a GUI app
app = Tk()
app.title("Mirror Mirror")
app.configure(bg="Black")
app.attributes('-fullscreen',True)
# Bind the app with Escape keyboard to
# quit app whenever pressed
app.bind('<Escape>', lambda e: app.quit())
  
# Create a label and display it on app
label_widget = Label(app)
label_widget.pack()

date = dt.datetime.now()
# Create Label to display the Date
label = Label(app, text=f"{date:%A, %B %d, %Y}", font="Calibri, 20", bg="Black", fg='White')
label.pack(pady=20)

# Create a function to open camera and
# display it in the label_widget on app
def AmazonSite():
    os.system('cmd /c start chrome "https://www.amazon.com" --disable-session-crashed-bubble --start-fullscreen')
    time.sleep(5)
    Onlyifyouknowhowtokill()
    
Amazonphoto = PhotoImage(file = r"C:\Users\Shweb\Desktop\Mirror Mirror\Icons\Amazon.png")
Amazonimage = Amazonphoto.subsample(3, 3)
Amazon = Button(image = Amazonimage, text="Amazon", command = AmazonSite, borderwidth=0, bg="Black")
Amazon.pack(side=LEFT)
  
def YoutubeSite():
    os.system('cmd /c start chrome "https://www.youtube.com" --disable-session-crashed-bubble --start-fullscreen')
    time.sleep(5)
    Onlyifyouknowhowtokill()
    
Youtubephoto = PhotoImage(file = r"C:\Users\Shweb\Desktop\Mirror Mirror\Icons\youtube.png")
Youtubeimage = Youtubephoto.subsample(3, 3)
Youtube = Button(image = Youtubeimage, text="Youtube", command = YoutubeSite, borderwidth=0, bg="Black")
Youtube.pack(side=LEFT)

def GmailSite():
    os.system('cmd /c start chrome "https://www.gmail.com" --disable-session-crashed-bubble --start-fullscreen')
    time.sleep(5)
    Onlyifyouknowhowtokill()
    
Gmailphoto = PhotoImage(file = r"C:\Users\Shweb\Desktop\Mirror Mirror\Icons\gmail.png")
Gmailimage = Gmailphoto.subsample(20, 20)
Gmail = Button(image = Gmailimage, text="Gmail", command = GmailSite, borderwidth=0, bg="Black")
Gmail.pack(side=LEFT)

def FacebookSite():
    os.system('cmd /c start chrome "https://www.facebook.com" --disable-session-crashed-bubble --start-fullscreen')
    time.sleep(5)
    Onlyifyouknowhowtokill()

Facebookphoto = PhotoImage(file = r"C:\Users\Shweb\Desktop\Mirror Mirror\Icons\facebook.png")
Facebookimage = Facebookphoto.subsample(12, 12)
Facebook = Button(image = Facebookimage, text="Facebook", command = FacebookSite, borderwidth=0, bg="Black")
Facebook.pack(side=LEFT)

def SteamApp():
    os.system('cmd /c start /d "C:\Program Files (x86)\Steam\" Steam.exe /wait /b "steam://open/bigpicture"')
    time.sleep(5)
    Onlyifyouknowhowtokill()
    
Steamphoto = PhotoImage(file = r"C:\Users\Shweb\Desktop\Mirror Mirror\Icons\Steam.png")
Steamimage = Steamphoto.subsample(4, 4)
Steam = Button(image = Steamimage, text="Steam", command = SteamApp, borderwidth=0, bg="Black")
Steam.pack(side=LEFT)

def DiscordApp():
    os.system('cmd /c start chrome "https://www.discord.com" --disable-session-crashed-bubble --start-fullscreen')
    time.sleep(5)
    Onlyifyouknowhowtokill()
    
Discordphoto = PhotoImage(file = r"C:\Users\Shweb\Desktop\Mirror Mirror\Icons\discord.png")
Discordimage = Discordphoto.subsample(10, 10)
Discord = Button(image = Discordimage, text="Discord", command = DiscordApp, borderwidth=0, bg="Black")
Discord.pack(side=LEFT)

def Onlyifyouknowhowtokill():
    os.system(r'cmd /c start /d "C:\Users\Shweb\Desktop\Mirror Mirror" MirrorMirrorCheck.vbs')
    time.sleep(3600)
        
def open_camera():
  
    # Capture the video frame by frame
    _, frame = vid.read()
  
    # Convert image from one color space to other
    opencv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
  
    # Capture the latest frame and transform to image
    captured_image = Image.fromarray(opencv_image)
  
    # Convert captured image to photoimage
    photo_image = ImageTk.PhotoImage(image=captured_image)
  
    # Displaying photoimage in the label
    label_widget.photo_image = photo_image
  
    # Configure image in the label
    label_widget.configure(image=photo_image)
  
    # Repeat the same process after every 10 seconds
    label_widget.after(10, open_camera)
    

open_camera()
app.mainloop()
