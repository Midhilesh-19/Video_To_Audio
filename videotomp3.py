import os
import moviepy.editor as mp #pip install moviepy

path = input("Enter the path of file :- ") #file path location and file name with "/"

videoclip = mp.VideoFileClip(path)
audioclip = videoclip.audio
audioclip.write_audiofile("12.mp3".format(path))#by using this the file will be coverted at the location place of code folder
               #or
#audioclip.write_audiofile("{}"12.mp3".format(path))''(this line will locate the converted file in where the actual video folder )''
