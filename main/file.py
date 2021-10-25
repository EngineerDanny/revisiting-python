
import sys

def open_file():
    try:      
      file = open('readme.txt')
      file.readline()
      i = int(file.strip())
   
    except:
      print('An exception occurred')

 
open_file()
