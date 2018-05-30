import sqlite3
import os


class Database:
    def connect(self):
        dataConnection = sqlite3.connect(".\\dinoData\\dinoData.db")
        self.cursor = dataConnection.cursor()

    def baseTable(self): 
        query = "CREATE TABLE IF NOT EXISTS dinoData(dino TEXT, Health REAL, Stamina REAL, Oxygen REAL, Food REAL, Weight REAL, Melee REAL, Speed Real)"
        self.cursor.execute(query)
        self.cursor.commit()

    def pullFromTable(self, creature):
        statement = "SELECT {0} FROM {0}".format(creature)
        self.cursor.execute(statement)

    def insertBaseData(self, tableName):
        
