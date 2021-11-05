
import shutil

path = "/Users/newuser/Projects/Personal/python/files/new_file.txt"

def write_file():
    try:
      with open(path, 'w') as file:
        file.write("Hello world\nThis is a document I created just for fun")
      print("File written successfully hurray")  
    except:
      print('An exception occurred')

def copy_paste_file():
  src = "/Users/newuser/Projects/Personal/python/new_file.txt"
  dst = "/Users/newuser/Projects/Personal/python/files"

  try:
      # shutil.copy2(src, dst) //This is for copy and pasting
      shutil.rmtree(dst)
  except Exception as e:
    print(e)
    print('An exception occurred')

copy_paste_file()
