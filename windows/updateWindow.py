from tkinter import *
import os
import dataGather.gather as gather


class Window:
    
    def __init__(self, master, dinoList, dataMenuUpdate, text):
        self.dinoList = dinoList
        self.dataMenuUpdate = dataMenuUpdate
        self.text = text

        maps = ['The Island', 'Scorched Earth', 'The Center', 'Ragnarok', 'Aberration']

        ######### Window to Obtain Directory #########

        dirWindow = Toplevel()
        dirWindow.title("Save Directory")
        #dirWindow.geometry('400x200')
        dirWindowFrame = Frame(dirWindow, width = '400')
        dirWindowFrame.pack()
        dirWindowFrameB = Frame(dirWindow)
        dirWindowFrameB.pack()

        ######### Sets Up Field to Enter Directory #########

        dwLabel = Label(dirWindowFrame, text = "Enter Ark save directory:")
        dwLabel.pack( side = 'left' )

        dwEntry = Entry(dirWindowFrame)
        dwEntry.pack( side = 'right', fill = 'x' )
        
        dirWindow.lift()
        dirWindow.attributes('-topmost', True)

        ######### Sets Up Map Dropdown #########

        selectedMap = StringVar()
        selectedMap.set(maps[0])

        dirMapType = OptionMenu(dirWindowFrameB, selectedMap, *maps)
        dirMapType.pack()

        ######### Adds button to confirm selection #########
        dd = gather.DinoData()

        dirButton = Button(dirWindow, text = 'Submit', command = lambda: [dd.grabDir(dwEntry.get(), selectedMap.get()), self.dinoList(self.text), self.dataMenuUpdate(), dirWindow.destroy()])
        dirButton.pack(side = 'bottom')

        dirWindow.mainloop()