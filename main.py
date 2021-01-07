import os, shutil
import tkinter
from tkinter import *
from tkinter import ttk, filedialog
from tkinter import messagebox

path = ''


def music():
    try:
        os.mkdir(path + '/Music')
    except FileExistsError:
        print('Cannot create a file when that file already exists: Music')
    finally:
        for file in os.listdir(path):
            try:
                splitted = file.rsplit('.')[-1]
                if splitted == 'mp3':
                    shutil.move(path + '/' + file, path + '/Music')
            except:
                tkinter.messagebox.showwarning(title="Something Went Wrong",
                                                message="There is two file with same name: " + file)

def video():
    try:
        os.mkdir(path + '/Video')
    except FileExistsError:
        print('Cannot create a file when that file already exists: Video')
    finally:
        for file in os.listdir(path):
            try:
                splitted = file.rsplit('.')[-1]
                if splitted == 'mp4' or splitted == 'avi' or splitted == 'mpeg' or splitted == '3gp' or splitted == 'm3u' or splitted == 'm4a' or splitted == 'mkv':
                    shutil.move(path + '/' + file , path + '/Video')
            except:
                tkinter.messagebox.showwarning(title="Something Went Wrong",
                                                message="There is two file with same name: " + file)

def pics():
    try:
        os.mkdir(path + '/Picture')
    except FileExistsError:
        print('Cannot create a file when that file already exists: Picture')
    finally:
        for file in os.listdir(path):
            try:
                splitted = file.rsplit('.')[-1]
                if splitted == 'png' or splitted == 'jpeg' or splitted == 'jpg' or splitted == 'gif' or splitted == 'bmp':
                    shutil.move(path + '/' + file , path + '/Picture')
            except FileExistsError:
                print("Already exists")
                continue

def compressed():
    try:
        os.mkdir(path + '/Compressed')
    except FileExistsError:
        print('Cannot create a file when that file already exists: Compressed')
    finally:
        for file in os.listdir(path):
            try:
                splitted = file.rsplit('.')[-1]
                if splitted == 'zip' or splitted == 'rar' or splitted == '7z' or splitted == 'ZIP':
                    shutil.move(path + '/' + file , path + '/Compressed')
            except:
                tkinter.messagebox.showwarning(title="Something Went Wrong", message="There is two file with same name: "+ file )

def text():
    try:
        os.mkdir(path + '/Text')
    except FileExistsError:
        print('Cannot create a file when that file already exists: Text')
    finally:
        for file in os.listdir(path):
            try:
                splitted = file.rsplit('.')[-1]
                if splitted == 'txt':
                    shutil.move(path + '/' + file , path + '/Text')
            except:
                tkinter.messagebox.showwarning(title="Something Went Wrong",
                                                message="There is two file with same name: " + file)

def office():
    try:
        os.mkdir(path + '/Office')
    except FileExistsError:
        print('Cannot create a file when that file already exists: Office')
    finally:
        for file in os.listdir(path):
            try:
                splitted = file.rsplit('.')[-1]
                if splitted == 'csv' or splitted == 'doc' or splitted == 'docx' or splitted == 'accdb' or splitted == 'pptx' or splitted == 'pub' or splitted == 'rtf' or splitted == 'xls' or splitted == 'xlsx':
                    shutil.move(path + '/' + file , path + '/Office')
            except:
                tkinter.messagebox.showwarning(title="Something Went Wrong",
                                               message="There is two file with same name: " + file)

def pdf():
    try:
        os.mkdir(path + '/Pdf')
    except FileExistsError:
        print('Cannot create a file when that file already exists: Pdf')
    finally:
        for file in os.listdir(path):
            try:
                splitted = file.rsplit('.')[-1]
                if splitted == 'pdf':
                    shutil.move(path + '/' + file , path + '/Pdf')
            except:
                tkinter.messagebox.showwarning(title="Something Went Wrong",
                                                message="There is two file with same name: " + file)

def exe():
    try:
        os.mkdir(path + '/Exe')
    except FileExistsError:
        print('Cannot create a file when that file already exists: Exe')
    finally:
        for file in os.listdir(path):
            try:
                splitted = file.rsplit('.')[-1]
                if splitted == 'exe' or splitted == 'msi':
                    shutil.move(path + '/' + file, path + '/Exe')
            except:
                tkinter.messagebox.showwarning(title="Something Went Wrong",
                                                message="There is two file with same name: " + file)

def jars():
    try:
        os.mkdir(path + '/Jars')
    except FileExistsError:
        print('Cannot create a file when that file already exists: Jars')
    finally:
        for file in os.listdir(path):
            try:
                splitted = file.rsplit('.')[-1]
                if splitted == 'jar':
                    shutil.move(path + '/' + file, path + '/Jar')
            except:
                tkinter.messagebox.showwarning(title="Something Went Wrong",
                                                message="There is two file with same name: " + file)

def java():
    print(path)
    try:
        os.mkdir(path + '/JavaClasses')
    except FileExistsError:
        print('Cannot create a file when that file already exists: JavaClasses')
    finally:
        for file in os.listdir(path):
            try:
                splitted = file.rsplit('.')[-1]
                if splitted == 'java':
                    shutil.move(path + '/' + file, path + '/JavaClasses')
            except:
                tkinter.messagebox.showwarning(title="Something Went Wrong",
                                                message="There is two file with same name: " + file)

class FolderSelect(Frame):
    def __init__(self,parent=None,folderDescription="",**kw):
        Frame.__init__(self,master=parent,**kw)
        self.folderPath = StringVar()
        self.lblName = Label(self, text=folderDescription)
        self.lblName.grid(row=0,column=0)
        self.entPath = Entry(self, textvariable=self.folderPath)
        self.entPath.grid(row=0,column=1)
        self.btnFind = ttk.Button(self, text="Browse Folder",command=self.setFolderPath)
        self.btnFind.grid(row=0,column=0)

    def setFolderPath(self):
        folder_selected = filedialog.askdirectory()
        self.folderPath.set(folder_selected)
    @property
    def folder_path(self):
        return self.folderPath.get()

def main():
    def setpath():
        global path
        path = directory1Select.folder_path
        print(path)

    window = Tk()

    window.title("File Manager")

    window.minsize(360, 350)
    window.maxsize(360, 350)

    pathsetbutton = Button(window, text="Set", height=1, width=7, command=setpath)

    info = Label(window,
                 text= "This is a file manager.\n Push the button which category you want.")

    jarbutton = Button(window, text=".jar",height = 1, width=7, command=jars)
    javabutton = Button(window, text=".java",height = 1, width=7, command=java)
    exebutton = Button(window, text=".exe",height = 1, width=7, command=exe)
    pdfbutton = Button(window, text=".pdf",height = 1, width=7, command=pdf)
    officebutton = Button(window, text="Office",height = 1, width=7, command=office)
    textbutton = Button(window, text=".txt",height = 1, width=7, command=text)
    compressedbutton = Button(window, text="Compressed",height = 1, width=7, command=compressed)
    picsbutton = Button(window, text="Image",height = 1, width=7, command=pics)
    videobutton = Button(window, text="Video",height = 1, width=7, command=video)
    musicbutton = Button(window, text="Music",height = 1, width=7, command=music)

    exitbutton = Button(window, text= "Exit", height = 1, width=7, command=exit)

    directory1Select = FolderSelect(window, "Select Path")
    directory1Select.place(x=10,y=200)



    info.place(x=65,y=1)
    pathsetbutton.place(x=150,y=230)

    jarbutton.place(x=10, y=100)
    javabutton.place(x=80, y=100)
    exebutton.place(x=150, y=100)
    pdfbutton.place(x=220, y=100)
    officebutton.place(x=290, y=100)

    textbutton.place(x=10, y=150)
    compressedbutton.place(x=80, y=150)
    picsbutton.place(x=150, y=150)
    videobutton.place(x=220, y=150)
    musicbutton.place(x=290, y=150)

    exitbutton.place(x=150, y=320)



    window.mainloop()
if __name__ == "__main__":
    main()