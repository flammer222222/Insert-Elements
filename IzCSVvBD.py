import sqlite3
import pandas as pd




tables = pd.read_csv('trans.csv', sep=';',encoding="utf_8")
ID_list=list(tables['Element_ID'])
Type_list=list(tables['TwotTyp'])

con = sqlite3.connect('TypeTr.db')
cursorObj = con.cursor()
for i in range(len(Type_list)):
	cursorObj.execute("INSERT INTO TypeTr VALUES ({0},{1})".format(ID_list[i],'"'+Type_list[i].strip()+'"'))
con.commit()
con.close()

# print(ID_list)
# print(Type_list)