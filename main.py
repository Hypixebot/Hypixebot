import subprocess
import os
import time
from datetime import datetime
import sys
now = datetime.now()
t=now.strftime('%I:%M:%p')
print(t)	

inp = subprocess.getoutput("termux-speech-to-text")
time.sleep(1)
print("\033[95m You said: ",str(inp))

def system():
     if inp == "":
         subprocess.call(["termux-tts-speak","please tell something sir"])

     elif "hello" in inp:
         subprocess.call(["termux-tts-speak","hallow sir "])
         
     elif "close" in inp:
         subprocess.call(["termux-tts-speak","ok sir wait a minute"])
         time.sleep(1)
         sys.exit()
     elif "how are you" in inp:
        subprocess.call(["termux-tts-speak","i am good sir "])
     elif "battery" in inp:
         subprocess.call(["termux-battery-status"])
         
     elif "sleep" in inp:
         subprocess.call(["termux-tts-speak","ok sir i am going to sleep for 5 second"])
         time.sleep(5)
         
     elif "call me" in inp:
         os.system("termux-telephony-call +91")
     elif "torch on" in inp:
         os.system("termux-torch on")
     elif "torch off" in inp:
         os.system("termux-torch off")

     elif "YouTube" in inp:
         os.system("termux-open https://m.youtube.com")
    
     elif "Google" in inp:
         os.system("termux-open https://www.google.co.in/")    
       
     elif "contact" in inp:
         os.system("termux-contact-list")
         
     elif "hai" in inp:
         subprocess.call(["termux-tts-speak","jaai raam ji ki saare milke bolo jaai raam ji ki"])
         
     elif "who are you" in inp:
          subprocess.call(["termux-tts-speak","I am your virtual assistanct, sir"])
    
     elif "time" in inp:
         subprocess.call(["termux-tts-speak",t])
         
     elif "what are you doing" in inp:
        subprocess.call(["termux-tts-speak","i am busy with you "])
        
     elif "are you busy" in inp:
         subprocess.call(["termux-tts-speak","i am always free for you"])
     
     elif "name" in inp:
         subprocess.call(["termux-tts-speak","my name is mathurm i know listening this name is very chaay but i like this because this is the combination of aaayyush's dada and dadi's name "])
     
     elif "give today's message" in inp:
           subprocess.call(["termux-tts-speak","computer is not a bad use if you use in a right way"])
     
     elif "are you in love" in inp:
           subprocess.call(["termux-tts-speak","aammmm,ammmmmam yes i am in a love with chithi"])
     
     elif "who made you" in inp:
         subprocess.call(["termux-tts-speak","made by AYUSH KUMAR BARNWAL"])
     elif "video" in inp:
         os.system("termux-open https://www.google.com/search?q=video")
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     else:
       subprocess.call(["termux-tts-speak","I am not cooded for that"])

system()

os.system("python main.py")
