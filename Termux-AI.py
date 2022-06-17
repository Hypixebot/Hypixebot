import time
Import date
import datetime
import os
import subprocess

os.system('screenfetch')
print('\033[1m' + '\033[91m'+'     ///   CREATED BY AYUSH KUMAR BARNWAL   ///')
def wish():
  h=int(datetime.datetime.now().hour)
  if h<12:
     subprocess.call(["termux-tts-speak","Good morning sir","how may i help you sir"])
  else:
     if h>=12 and h<17:
       subprocess.call(["termux-tts-speak","good afternoon sir","how may i help you sir"])
     elif h>=17 and h<20:
       subprocess.call(["termux-tts-speak","good evening sir,how may i help you sir"])
     else:
       subprocess.call(["termux-tts-speak","welcome sir how may i help you sir"])
wish()
os.system("python main.py")
