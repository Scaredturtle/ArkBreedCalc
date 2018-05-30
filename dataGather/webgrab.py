import requests
import bs4
from tkinter import *
import pandas as pd


class dataSitePull:
    def pullParentTable(self, text):
        headers = []
        url = 'https://ark.gamepedia.com/Creatures'
        request = requests.get(url)
        
        #this line below makes it legible
        parsedText = bs4.BeautifulSoup(request.text, 'html.parser')#.findAll('tr', attrs={'align':'left'})
        dinoParse = parsedText.findAll('tr', attrs={'align':'left'})
        dinotable = parsedText.find('table', attrs = {'class':'wikitable sortable'})
        headersHTML = dinotable.findAll('th')

        text.insert(END, headersHTML)       