import os
import tkinter as tk

root= tk.Tk()
root.resizable(0,0)
root.title("Python Packages Installer")

canvas1 = tk.Canvas(root,highlightthickness=0, width = 300, height = 410, bg="SteelBlue4", relief = 'raised')
canvas1.pack()

label1 = tk.Label(root, text='Name of the library:', bg="SteelBlue4", fg="white")
label1.config(font=('helvetica', 16))
canvas1.create_window(150, 80, window=label1)

entry1 = tk.Entry (root, width =20)
entry1.config(font=("helvetica",16))
canvas1.create_window(150,120, window=entry1)


def installPackage ():
    global installPythonPackage
    installPythonPackage = 'pip install ' + entry1.get()
    
    os.system('start cmd /k ' + installPythonPackage)


def uninstallPackage ():
    global uninstallPythonPackage
    uninstallPythonPackage = 'pip uninstall ' + entry1.get()
    
    os.system('start cmd /k ' + uninstallPythonPackage)

def updatePipPackage ():
    global updatePIPpackage
    updatePIPpackage = 'pip install --upgrade pip'
    
    os.system('start cmd /k ' + updatePIPpackage)

def updatePackage():
    global updatePythonPackage
    updatePythonPackage = 'pip install --upgrade ' + entry1.get()

    os.system('start cmd /k ' + updatePythonPackage)

def listPackages():
    global listPythonPackages
    listlibs= 'pip list'

    os.system('start cmd /k '+ listlibs)

def versionPackage ():
    global versionPIPpackage
    versionPIPpackage = 'pip --version'
    
    os.system('start cmd /k ' + versionPIPpackage)

    
button1 = tk.Button(text='      Install     ', command=installPackage, bg='green', fg='white', font=('helvetica', 14, 'bold'))
canvas1.create_window(80, 180, window=button1)


button2 = tk.Button(text='   Uninstall   ', command=uninstallPackage, bg='crimson', fg='white', font=('helvetica', 14, 'bold'))
canvas1.create_window(80, 230, window=button2)

button3 = tk.Button(text='     Update    ', command=updatePackage, bg='maroon', fg='white', font=('helvetica', 14, 'bold'))
canvas1.create_window(80, 280, window=button3)

button4 = tk.Button(text=' Update Pip ', command=updatePipPackage, bg='blue', fg='white', font=('helvetica', 14, 'bold'))
canvas1.create_window(220, 180, window=button4)

button5 = tk.Button(text='    List libs    ', command=listPackages, bg='violet', fg='white', font=('helvetica', 14, 'bold'))
canvas1.create_window(220, 230, window=button5)

button6 = tk.Button(text='    Version    ', command=versionPackage, bg='orange', fg='white', font=('helvetica', 14, 'bold'))
canvas1.create_window(220.5, 280, window=button6)

root.mainloop()