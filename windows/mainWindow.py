from tkinter import *
from tkinter.ttk import *
from windows.updateWindow import *
import dinoData.display as display
import dataGather.webgrab as web


class MainWindow:
    
    def initWindow(self):
        self.master.geometry('200x200')
        rows = 0
        while rows < 10:
            self.master.rowconfigure(rows, weight = 1)
            self.master.columnconfigure(rows, weight = 1)
            rows += 1
    
    def runUpdateWindow(self):
        Window.__init__(self.master)
    
    def dinoList(self, text):
        text.delete('1.0', END)
        for entry in range(len(self.types)):
            text.insert(END, "Class: " + self.types[entry] + "\n")
            text.insert(END, "Name: " + self.names[entry] + "\n\n")
    
    def dropDownInit(self):
        self.selectedDino = StringVar()
        self.selectedDino.set(self.names[0])

    def dinoDataMenuUpdate(self):
        pass
        #menu = self.dinoDataMenu['menu']
        #menu.delete(0, "end")
        #menu.add(list, self.names)
    
    def __init__(self, master, types, names, files):
        self.master = master
        self.types = types
        self.names = names
        self.files = files

        self.initWindow()

        dinoNotebook = Notebook(self.master)
        dinoNotebook.grid(row = 1, column = 0, columnspan = 10, rowspan = 9, sticky = 'NESW')

        dodoFrame = Frame(dinoNotebook)

        dinoNotebook.add(dodoFrame, text = 'Dodo')
        
        #topFrame = Frame(master)
        #topFrame.pack()

        #dinoFrame = Frame(master)
        #dinoFrame.pack()

        #textFrame = Frame(master)
        #textFrame.pack()

        #self.text = Text(textFrame)
        #self.text.pack()

        #updateButton = Button(topFrame, text = "Update List", command = lambda: Window(master, self.dinoList, self.dinoDataMenuUpdate, self.text))
        #updateButton.grid(row = 0, column = 0)

        #dinoTypeButton = Button(topFrame, text = "List Dino Types", command = lambda: self.dinoList(self.text))
        #dinoTypeButton.grid(row = 0, column = 1)

        #self.dropDownInit()

        #datadis = display.DisplayData()

        #self.dinoDataMenu = OptionMenu(dinoFrame, self.selectedDino, *self.names, command = lambda x: datadis.displaySelected(self.text, self.selectedDino.get(), self.files))
        #self.dinoDataMenu.pack()

        #parentdata = web.dataSitePull()
        #parentdata.pullParentTable(self.text)

        #self.dinoLB = Listbox(dinoFrame)

        #self.dinoDataButton = Button(topFrame, text = "Dino Data", command = self.fileData)
        #self.dinoDataButton.grid(row = 0, column = 2)

        master.mainloop()