import sqlite3
import csv
import pandas as pd

csv_path = "inputData.csv"
tables = pd.read_csv(csv_path, sep=';',encoding="utf_8")

Names=list(tables["ТП"])
Sn=list(tables['Sнагр'])
print(Names)
print(Sn)
print("Введите исходную нагрузку")
mystring=input()
Flag_Lf=4
path_database="R:/2. Моделирование - группа/3 СОТРУДНИКИ/Алексей/проекты/TrLoad_files/database.db"
con = sqlite3.connect(path_database)
cursorObj = con.cursor()

for i in range(len(Names)):
	# try:
	# 	print(cursorObj.execute("SELECT  Element_ID FROM Element WHERE Type='Load' and Name={0}".format('"'+Names[i]+'"')).fetchall()[0][0])
	# 	cursorObj.execute('UPDATE Load WHERE SET UI = {0}'.format(Flag_Lf))
	# except:
	# 	print("rtr")
	Element_ID=cursorObj.execute("SELECT  Element_ID FROM Element WHERE Type='Load' and Name={0}".format("'"+Names[i]+"'")).fetchall()[0][0]
	print(Element_ID)
	cursorObj.execute('UPDATE Load SET Flag_Lf = {0} WHERE Element_ID={1}'.format(Flag_Lf,Element_ID))
	cursorObj.execute('UPDATE Load SET Ul = {0} WHERE Element_ID={1}'.format(float(Sn[i].replace(",",".")),Element_ID))
con.commit()	
con.close()