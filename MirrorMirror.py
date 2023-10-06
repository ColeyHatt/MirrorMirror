import tkinter as tk
import os
import datetime as dt
import time
import keyboard
import random
import tkinterweb
website = "www.google.com"
app = tk.Tk()
app.title("Mirror Mirror")
app.configure(bg="Black")
app.attributes('-fullscreen',True)
app.iconbitmap(r"C:\Users\Shweb\Desktop\MirrorMirror\Icons\Logo.ico")
random = random.randint(1, 6)
workouts = ["Crunches", "Pushups", "Situps", "Mile Run", "Curls", "Turtles"]
Name = tk.Label(app, text="Mirror Mirror", font="20", bg="Black", fg='White')
Name.pack()

AuthorName = tk.Label(app, text="Coley Hatt © 2023", font="20", bg="Black", fg='White')
AuthorName.pack(side=tk.BOTTOM)

date = dt.datetime.now()
time = tk.Label(app, text=f"{date:%A, %B %d, %Y}", font="20", bg="Black", fg='White')
time.pack()

frame = tkinterweb.HtmlFrame(app, messages_enabled = False)
frame.load_website(f"{website}")
frame.pack(side=tk.TOP)

Choice = tk.Label(app, text="HTML Viewer", font="20", bg="Black", fg='White')
Choice.pack()


def AmazonSite():
    os.system(r'cmd /c start chrome "https://www.amazon.com" --disable-session-crashed-bubble --start-fullscreen')
    
Amazonphoto = tk.PhotoImage(file = r"C:\Users\Shweb\Desktop\MirrorMirror\Icons\Amazon.png")
Amazonimage = Amazonphoto.subsample(3, 3)
Amazon = tk.Button(image = Amazonimage, text="Amazon", command = AmazonSite, borderwidth=0, bg="Black")
Amazon.pack(side=tk.LEFT)
  
def YoutubeSite():
    os.system(r'cmd /c start chrome "https://www.youtube.com" --disable-session-crashed-bubble --start-fullscreen')
    
Youtubephoto = tk.PhotoImage(file = r"C:\Users\Shweb\Desktop\MirrorMirror\Icons\youtube.png")
Youtubeimage = Youtubephoto.subsample(3, 3)
Youtube = tk.Button(image = Youtubeimage, text="Youtube", command = YoutubeSite, borderwidth=0, bg="Black")
Youtube.pack(side=tk.LEFT)

def GmailSite():
    os.system(r'cmd /c start chrome "https://www.gmail.com" --disable-session-crashed-bubble --start-fullscreen')
    
Gmailphoto = tk.PhotoImage(file = r"C:\Users\Shweb\Desktop\MirrorMirror\Icons\gmail.png")
Gmailimage = Gmailphoto.subsample(20, 20)
Gmail = tk.Button(image = Gmailimage, text="Gmail", command = GmailSite, borderwidth=0, bg="Black")
Gmail.pack(side=tk.LEFT)

def FacebookSite():
    os.system(r'cmd /c start chrome "https://www.facebook.com" --disable-session-crashed-bubble --start-fullscreen')

Facebookphoto = tk.PhotoImage(file = r"C:\Users\Shweb\Desktop\MirrorMirror\Icons\facebook.png")
Facebookimage = Facebookphoto.subsample(12, 12)
Facebook = tk.Button(image = Facebookimage, text="Facebook", command = FacebookSite, borderwidth=0, bg="Black")
Facebook.pack(side=tk.LEFT)

def SteamApp():
    os.system(r'cmd /c start /d "C:\Program Files (x86)\Steam\" Steam.exe /wait /b "steam://open/bigpicture"')
    
Steamphoto = tk.PhotoImage(file = r"C:\Users\Shweb\Desktop\MirrorMirror\Icons\Steam.png")
Steamimage = Steamphoto.subsample(4, 4)
Steam = tk.Button(image = Steamimage, text="Steam", command = SteamApp, borderwidth=0, bg="Black")
Steam.pack(side=tk.LEFT)

def NotepadApp():
    os.system(r'cmd /c start /d "C:\Program Files\Notepad++\" notepad++.exe')
    
    
Notepadphoto = tk.PhotoImage(file = r"C:\Users\Shweb\Desktop\MirrorMirror\Icons\Notepad++.png")
Notepadimage = Notepadphoto.subsample(4, 4)
Notepad = tk.Button(image = Notepadimage, text="Notepad", command = NotepadApp, borderwidth=0, bg="Black")
Notepad.pack(side=tk.LEFT)

def DiscordSite():
    os.system(r'cmd /c start chrome "https://www.discord.com" --disable-session-crashed-bubble --start-fullscreen')
    
Discordphoto = tk.PhotoImage(file = r"C:\Users\Shweb\Desktop\MirrorMirror\Icons\discord.png")
Discordimage = Discordphoto.subsample(10, 10)
Discord = tk.Button(image = Discordimage, text="Discord", command = DiscordSite, borderwidth=0, bg="Black")
Discord.pack(side=tk.LEFT)

os.system(r'cmd /c start "C:\Windows\System32" osk.exe')

def die():
    os.system(r'cmd /c start /d "C:\Users\Shweb\Desktop\MirrorMirror\" MirrorMirrorCheck.vbs')

def Workout():
   top= Toplevel(app)
   top.geometry("750x250")
   top.title(f"Workouts")
   Label(top, text= f"{workouts[random]}", font=('Mistral 18 bold')).place(x=150,y=80)

Workout = tk.Button(text="Workout", command = Workout, bg="Black")
Workout.pack(side=tk.LEFT)

keyboard.on_press_key("`", lambda _:die())
app.bind('<Home>', lambda e: quit())
app.mainloop()
