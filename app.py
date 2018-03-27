import os
import tkinter
import json
from pprint import pprint

root = tkinter.Tk()

def updateDino():
    os.system('java -jar C:\\Users\\Aaron\\Desktop\\Ark\\Ark_self_made_mods\\ark-tools.jar tamed --clean C:\\Users\\Aaron\\Desktop\\Ark\\Server\\Servers\\Server1\\ShooterGame\\Saved\\SavedArks\\Ragnarok.ark .\\JSON --pretty-printing')

def dinoList():
    textDisplay.delete('1.0', tkinter.END)
    clfile = open('.\\JSON\\classes.json')
    dinocl = json.load(clfile)
    for data in dinocl:
        for k, v in data.items():
            if k == "cls":
                textDisplay.insert(tkinter.END, "Class: {} \n".format(v))
            else:
                textDisplay.insert(tkinter.END, "Name: {} \n\n".format(v))

topFrame = tkinter.Frame(root)
topFrame.pack()

dinoFrame = tkinter.Frame(root)
dinoFrame.pack()

textFrame = tkinter.Frame(root)
textFrame.pack()

textDisplay = tkinter.Text(textFrame)
textDisplay.pack()

updateButton = tkinter.Button(topFrame, text = "Update List", command = updateDino)
updateButton.grid(row = 0, column = 0)

dinoTypeButton = tkinter.Button(topFrame, text = "List Dino Types", command = dinoList)
dinoTypeButton.grid(row = 0, column = 1)

root.mainloop()