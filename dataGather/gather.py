import json
import os


class DinoData:
    def initDino(self):
        workingDir = os.path.join(".", "JSON")
        tameTypes = []
        tameFiles = []
        typeNames = []

        clfile = open(os.path.join(workingDir, "classes.json"), 'r')
        dinocl = json.load(clfile)
        clfile.close()
        del tameTypes[:]
        del tameFiles[:]
        del typeNames[:]
        print(typeNames)
        print(tameTypes)
        print(tameFiles)
        for data in dinocl:
            for k, v in data.items():
                if k == "cls":
                    tameTypes.append(v)
                    tameFiles.append(v + ".json")
                else:
                    typeNames.append(v)

        print(typeNames)
        print(tameTypes)
        print(tameFiles)

        return typeNames, tameTypes, tameFiles

    def grabDir(self, path, ark):
        print (path)

        ## Sets the selected map to match file syntax ##
        ark = ark.replace(' ', '')
        if ark == 'Aberration':
            ark = ark + '_P'
        print (ark)
        ark = ark + '.ark'
        print (ark)

        if ark != None:
            os.system('java -jar .\\tools\\ark-tools.jar tamed --clean C:\\Users\\Aaron\\Desktop\\Ark\\Server\\Servers\\Server1\\ShooterGame\\Saved\\SavedArks\\{0} .\\JSON --pretty-printing'.format(ark))
