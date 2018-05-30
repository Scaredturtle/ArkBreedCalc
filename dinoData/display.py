from tkinter import *
import os
import json


class DisplayData:
    def displaySelected(self, text, selection, files):
        jsonDir = ".\\JSON\\"
        for dfile in files:
            if selection[:4] in dfile:
                print (dfile)
                workingFile = os.path.join(jsonDir, dfile)
        
        dataFile = open(workingFile, mode = 'r')
        dinoDataFile = json.load(dataFile)
        dataFile.close()
        text.delete('1.0', END)
        for creature in dinoDataFile:
            text.insert(END, "Owner: {}\n".format(creature["tamer"]))
            text.insert(END, "Dino Type: {}\n".format(creature["type"]))
            for stats, value in creature["wildLevels"].items():
                text.insert(END, "{}: {}\n".format(stats, value))
            text.insert(END, "\n\n")