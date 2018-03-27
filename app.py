import os
import tkinter

root = tkinter.Tk()

def updateDino():
    os.system('java -jar C:\\Users\\Aaron\\Desktop\\Ark\\Ark_self_made_mods\\ark-tools.jar tamed C:\\Users\\Aaron\\Desktop\\Ark\\Server\\Servers\\Server1\\ShooterGame\\Saved\\SavedArks\\Ragnarok.ark C:\\Users\\Aaron\\Desktop\\Ark\\Ark_self_made_mods\\JSON --pretty-printing')

updateButton = tkinter.Button(root, text = "Update List", command = updateDino)
updateButton.grid(row = 0, column = 0)

root.mainloop()