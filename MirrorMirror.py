# Python program to open the
# camera in Tkinter
# Import the libraries,
# tkinter, cv2, Image and ImageTk
  
from tkinter import *
import cv2
from PIL import Image, ImageTk
from subprocess import Popen
import os
  
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
  
# Bind the app with Escape keyboard to
# quit app whenever pressed
app.bind('<Escape>', lambda e: app.quit())
  
# Create a label and display it on app
label_widget = Label(app)
label_widget.pack()

# Create a function to open camera and
# display it in the label_widget on app
def Amazon():
    os.system('cmd /c start chrome "https://www.amazon.com" --disable-session-crashed-bubble')
    
Amazon = Button(text="Amazon", command = Amazon)
Amazon.pack(side=LEFT)
  
def Youtube():
    os.system('cmd /c start chrome "https://www.youtube.com" --disable-session-crashed-bubble')
    
Youtube = Button(text="Youtube", command = Youtube)
Youtube.pack(side=LEFT)
  
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
