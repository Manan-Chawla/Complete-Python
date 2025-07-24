import os


cwd = os.getcwd()
print(f"The current directory is: {cwd}")

try:
    os.chdir("C:/Users/chawl/OneDrive/Desktop/pythontut/filedirs")
    print("✅ Directory changed successfully!")
    print(f"Now in: {os.getcwd()}")
except FileNotFoundError:
    print("❌ Directory not found. Please check the path.")
except Exception as e:
    print(f"⚠️ Error: {e}")
    
    
entries=os.listdir()
print(entries)



try:
    os.mkdir("bella")
    print("Folder 'bella' created.")
    
    os.makedirs("bella/newbella")
    print("Subfolder 'bella/newbella' created.")
except FileExistsError:
    print("Folder already exists.")
except Exception as e:
    print(f"Error while creating folder: {e}")

try:
    os.rmdir("bella/newbella")
    print("Subfolder 'newbella' removed.")
    os.rmdir("bella")
    print("Folder 'bella' removed.")
except FileNotFoundError:
    print("Folder not found.")
except OSError:
    print("Cannot remove non-empty folder.")
except Exception as e:
    print(f"Error: {e}")
    
    
path="file1.py"
if os.path.exists(path):
    print("yes it is")
else:
    print("no it's not")


os.path.isfile(path)
os.path.isdir(path)


name,ext=os.path.splitext(path)
print(name)
print(ext)


for root,dirs,files in os.walk("."):
    print(root)
    print(dirs)
    print(files)
