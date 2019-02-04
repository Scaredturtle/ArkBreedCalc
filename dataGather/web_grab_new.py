import os
import requests
import pandas as pd
import dinoData.dataBase as sql_data

class site_data_pull():
    def main_table_pull(self):
        sql_table_name = "Creatures"

        creature_table_url = "https://ark.gamepedia.com/Creatures"
        raw_HTML = requests.get(creature_table_url, headers={'User-Agent': 'Mozilla/5.0'})
        
        test_table = pd.read_html(raw_HTML.text, header = 0)
        #print (test_table[1].head(5))
        raw_table = test_table[1]
        raw_table.rename(columns={"Common / In Game NameName":"Name","TameableTame":"Tameable","Entity ID":"Entity_ID"}, inplace=True)
        #print (raw_table.head(5))
        raw_table.to_csv(os.path.join('.', 'test_data.csv'))
        modded_table = raw_table.drop(raw_table[raw_table.Tameable != 'Yes'].index)
        modded_table = modded_table.drop(['Released', 'Diet', 'Temperament', 'Tameable', 'RideableRide', 'BreedableBreed', 'Saddle LevelSaddle', 'Feces SizeFeces'], axis=1)
        modded_table = modded_table.drop(modded_table[modded_table.Group.str.contains("Creatures")].index)
        #modded_table = modded_table.drop(modded_table[modded_table.Group == 'Event Creatures'].index)
        modded_table = modded_table.drop(modded_table[modded_table.Name.str.contains(" - ")].index)
        modded_table = modded_table.reset_index(drop=True)
        print (modded_table.head(5))
        modded_table.to_csv(os.path.join('.', 'modded_data.csv'))

        connection = sql_data.Database()

        db_file, db_cursor = connection.create_connection()

        modded_table.to_sql(sql_table_name, db_file, if_exists = "replace")

        db_cursor = connection.new_cursor()

        pulled_table = pd.read_sql("SELECT * FROM %s;" %sql_table_name, db_file)

        print (pulled_table.head(3))

        connection.close_connection()

        
if __name__ == '__main__':
    site_data_pull().main_table_pull()
