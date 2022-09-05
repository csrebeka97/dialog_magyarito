from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename, askdirectory
import os
import zipfile
from pathlib import Path
import shutil

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename =askopenfilename(title="Válaszd ki az átalakítandó epub fájlt:") # show an "Open" dialog box and return the path to the selected file
new_file_name = filename.replace(".epub", ".zip")
os.rename(filename, new_file_name)

with zipfile.ZipFile(new_file_name, 'r') as zip_ref:
    folder = askdirectory(title="Válaszd ki, hova szeretnéd menteni a módosított fájlt:")
    head, tail = os.path.split(new_file_name)
    extract = os.path.join(folder, tail.replace(".zip",""))
    zip_ref.extractall(extract)

os.rename(new_file_name, filename) 

files = Path(extract).glob('**/*.html')
for file in files:
    with open(file, 'r',  encoding='utf-8') as f:
        data = f.read()
        data = data.replace('“',' - ')
        data = data.replace('”', ' - ') 
    with open(file, 'w', encoding='utf-8') as f:
        f.write(data)

target = os.path.join(folder, tail)
with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as zip_ref:
    for folder_name, subfolders, filenames in os.walk(extract):
        for filename in filenames:
            file_path = os.path.join(folder_name, filename)
            zip_ref.write(file_path, arcname=os.path.relpath(file_path, extract))
os.rename(target, target.replace(".zip", ".epub"))
shutil.rmtree(extract)
k  =input("Nyomd meg az x-et a kilépéshez:")