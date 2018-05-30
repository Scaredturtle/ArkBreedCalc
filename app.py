import tkinter
from pprint import pprint
from windows.mainWindow import *
import dataGather.sort as dsort
import dataGather.gather as gather

root = tkinter.Tk()
root.title('Ark Improved Dino Calculator')

    #textDisplay.insert(tkinter.END, dinoDataFile)

dd = gather.DinoData()
typeNames, tameTypes, tameFiles = dd.initDino()

pprint(typeNames)
pprint(tameTypes)
pprint(tameFiles)

ds = dsort.DinoSort()
typeNames = ds.nameSort(typeNames)
tameTypes = ds.nameSort(tameTypes)
tameFiles = ds.nameSort(tameFiles)

MainWindow(root, tameTypes, typeNames, tameFiles)

root.mainloop()