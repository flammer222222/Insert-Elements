import pandas as pd
import sqlite3
from Name_convertor import Convertor
class T_type (object):
	def __init__ (self,path_data,path_type_db):
		self.path_data=path_data
		self.path_type_db=path_type_db
		"""Constructor"""
	def get_T_type(self):
		_tables = pd.read_csv(self.path_data, sep=';',encoding="utf_8")
		_Type_name=[]
		_Name_Sn={}
		_u=list(_tables['U'])
		_TP=list(_tables['ТП'])
		_Strr=list(_tables['Sтр-р'])
		_Type=list(_tables['Тип'])
		_Ntr=list(_tables['Nтр'])
		for i in range(len(_TP)):
			_TP_name='ТП-'+_TP[i]+' '+_Ntr[i].strip().replace("Т-1","Т1").replace("Т-2","Т2")
			_Name=_Type[i].strip()+'-'+str(_Strr[i])+'/'+str(_u[i])
			_Name04=_Type[i].strip()+'-'+str(_Strr[i])+'/'+str(_u[i])+'/'+'0,4'
			_Type_name.append((_TP_name,_Name,_Name04))
			_Name_Sn[_Type_name[i][0]]=_Strr[i]
		self.Type_name=_Type_name
		self.Name_Sn=_Name_Sn
		
	def get_ID(self):
		self.get_T_type()
		_ID_TP_Name={}
		con = sqlite3.connect(self.path_type_db)
		cursorObj = con.cursor()
		for i in range(len(self.Type_name)):
			try:
				cursorObj.execute("SELECT * FROM TypeTr WHERE Name={0} or Name={1}".format('"'+self.Type_name[i][1]+'"','"'+self.Type_name[i][2]+'"'))
				_ID_TP_Name[self.Type_name[i][0]]=cursorObj.fetchall()[0][0]
			except:
				_ID_TP_Name[self.Type_name[i][0]]=1
		con.close()
		return(_ID_TP_Name)

	def get_Sn(self,Name):
		self.get_T_type()
		return self.Name_Sn.get(Name)
		
		# return self.Name_Sn

if __name__ == "__main__":
	Name=Convertor.name_convertor("ТП-2231 C1",0)
	path_type_db='TypeTr.db'
	path_data='Data.csv'
	ID=T_type(path_data,path_type_db)
	ID.get_ID()
	print(ID.get_Sn("ТП-45 Т"))
