import sqlite3
import os


class Database:
    def create_connection(self):
        self.database_file = sqlite3.connect(os.path.join(".", "dinoData", "dinoData.db"))
        self.cursor = self.database_file.cursor()
        
        return self.database_file, self.cursor

    def new_cursor(self):
        self.cursor.close()
        self.cursor = self.database_file.cursor()

        return self.cursor

    def close_connection(self):
        self.cursor.close()
        self.database_file.close()
        