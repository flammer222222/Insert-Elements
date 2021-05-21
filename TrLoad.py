import sqlite3
import sys
import os
import pandas as pd

path_database="R:/2. Моделирование - группа/3 СОТРУДНИКИ/Алексей/проекты/TrLoad_files/database.db"

def Add_Element_Load(path_database):
	Max_Element_ID=8
	con = sqlite3.connect(path_database)
	cursorObj = con.cursor()
	cursorObj.execute("INSERT INTO Element VALUES (10, 2, 1, 1, 1, 'NameLoad', 'ShortNameLOAD', 'Load', 3, 1, 1, 0, 0, 0.0, 0.0, 0.0, 0.0, 'None', 0.0, 'None', 0.0, 0.0, 0, 0, 0, 0, '', 'None', 1.0, 1.0)")
	con.commit()
	con.close()	
def Add_Load(path_database):
	Max_Element_ID=8
	con = sqlite3.connect(path_database)
	cursorObj = con.cursor()
	cursorObj.execute("INSERT INTO Load VALUES (10, 0, 1, 2, 1, 0.0, 0.0, 100.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1, 0, 0, 0, 0, 1, 1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1, 1.0, 0.0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.95, 1, 0.0, 0.75, 0, 0, 0, 1, 1, 0.0, 0.0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, 0.0, 0.0, 0.0, 0.0)")
	con.commit()
	con.close()
def Add_Load_Terminal(path_database):
	Max_Element_ID=8
	con = sqlite3.connect(path_database)
	cursorObj = con.cursor()
	cursorObj.execute("INSERT INTO Terminal VALUES 	(15, 10, 7, 1, 1, 1, 0.0, 0.0, 7, 1, 0, 0, 1, 0)")
	# cursorObj.execute("INSERT INTO Terminal VALUES (Terminal_ID,Element_ID,Node_ID,'1',Start or end(1 or 2),'1','0.0','0.0','7','1','0','0','1','0')")
	con.commit()
	con.close()
def Add_Graphic_Element_Load(path_database):
	Max_Element_ID=8
	con = sqlite3.connect(path_database)
	cursorObj = con.cursor()	
	cursorObj.execute("INSERT INTO GraphicElement VALUES (10, 1, 1, 37, 0, 10, 1, 0, -1, 0, 1, 100, 0.1124925, 0.1650000000000002, 13, 0, 0, 1, 1, 1, 0)")
	con.commit()
	con.close()
												#(Graphic_Element_ID, 1, 1,Graphic_text_ID, 0, Element_ID, 16777730, 0, -1, 0, 1, 100, CenterX, CenterY, 20, 0, 0, 1, 1, 1, 0)
def Add_Grafic_Element_terminal(path_database):
	Max_Element_ID=8
	con = sqlite3.connect(path_database)
	cursorObj = con.cursor()
	cursorObj.execute("INSERT INTO GraphicTerminal VALUES (15, 10, 38, 15, 0.1124925, 0.175, 0, 0, 1, 0, 4, 20.0, 80, -1, 0, 0, 0, 4, 0.4, 0, -1, 0, 0, 292, 0, 1, 1, 1, 0)")
					 #Точка присоединения к линии(Graphic_TErminal_ID,GraphicElement_ID,GraphicTExt_ID,Terminal_ID, PosX, PosY, 0, 0, 1, 0, 4, 20.0, 80, -1, 0, 0, 0, 4, 0.4, 0, -1, 0, 0, 292, 0, 1, 1, 1, 0)
	con.commit()
	con.close()
def Add_text_Load(path_database):
	Max_Element_ID=8
	con = sqlite3.connect(path_database)
	cursorObj = con.cursor()
	cursorObj.execute("INSERT INTO GraphicText VALUES (37, 1, 'Arial', 16, 9, 6, 0, 0, 1, 1, 0.0, -2.75e-05, 0.007500000000000001, 1, 0, 0, 1, 1)")
	cursorObj.execute("INSERT INTO GraphicText VALUES (38, 1, 'Arial', 16, 9, 0, 0, 0, 1, 1, 0.0, -2.75e-05, 0.007500000000000001, 1, 0, 0, 1, 1)")
	cursorObj.execute("INSERT INTO GraphicText VALUES (39, 1, 'Arial', 16, 9, 3, 0, 0, 1, 1, 0.0, -2.75e-05, 0.007500000000000001, 1, 0, 0, 1, 1)")
	cursorObj.execute("INSERT INTO GraphicText VALUES (40, 1, 'Arial', 16, 9, 3, 0, 0, 1, 1, 0.0, -2.75e-05, 0.007500000000000001, 1, 0, 0, 1, 1)")
	con.commit()
	con.close()
def Add_Element_TR(path_database):
	Max_Element_ID=8
	con = sqlite3.connect(path_database)
	cursorObj = con.cursor()
	cursorObj.execute("INSERT INTO Element VALUES (9, 2, 1, 1, 1, 'nameTR', 'ShortNameTR', 'TwoWindingTransformer', 3, 1, 1, 0, 0, 0.0, 0.0, 0.0, 0.0, 'None', 0.0, 'None', 0.0, 0.0, 0, 0, 0, 0, '', 'None', 1.0, 1.0)")
	# cursorObj.execute("INSERT INTO Element VALUES ('9','2', '1','1', '1','nameTR','ShortNameTR','TwoWindingTransformer','3','1','1','0','0','0.0','0.0','0.0','0.0','NULL','0.0','NULL','0.0','0.0','0','0','0','0','','NULL','1.0','1.0')")#,%Max_Element_ID)
	con.commit()
	con.close()
def Add_Node(path_database):
	Max_Element_ID=8
	con = sqlite3.connect(path_database)
	cursorObj = con.cursor()
	cursorObj.execute("INSERT INTO Node VALUES (7, 1, 1, 2, 'nameNode', 'ShortNameNode', 10.0, 1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0, 0, 1, 0.0, 0.0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 'None', 0.0, 'None', 0.0, 0, 0, 0, 0, 0.0, 0.0, 0, 7, 0, 2, 0.0, 0.0, 'None', 0.0, 0)")
	# cursorObj.execute("INSERT INTO Node VALUES ('7','1','1','2','nameNode','ShortNameNode','10.0','1','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0','1','','1','0','0','0','0','0','0','0','0','0.0','0','0','1','0.0','0.0','0','0','0','0','0.0','0.0','0.0','0.0','NULL','0.0','NULL','0.0','0','0','0','0','0.0','0.0','0','7','0','2','0.0','0.0','NULL','0.0','0')")
	con.commit()								
	con.close()
def Add_TR(path_database):
	Max_Element_ID=8
	con = sqlite3.connect(path_database)
	cursorObj = con.cursor()
	# cursorObj.execute("INSERT INTO TwoWindingTransformer VALUES ('9','0','0','10.0','10.0','0.0001','0.0','8.0','0.0','0.0','0.0','1.1','0.0','0.0','100.0','0.9','6','1','1','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0','0','1','0.0','0.0','0.0','1','0.0','0.0','0.0','0.0','0','103.0','98.0','1','1.0','0.0','0','0','0','0','0','0','0.0','0','3','0.0','0.0','0','0','0.0','0.0','0.0','0','16.0','0.0','0','0','2','0.0','0.0','0.0','0','0.0','0.1','0.05','0','0.0','0','0.0','0.0','0.0','0','0','1','1','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0','0','0','8','0','0','1','0','0')")
	cursorObj.execute("INSERT INTO TwoWindingTransformer VALUES (9, 0, 0, 10.0, 10.0, 0.0001, 0.0, 8.0, 0.0, 0.0, 0.0, 1.1, 0.0, 0.0, 100.0, 0.9, 6, 1, 1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 1, 0.0, 0.0, 0.0, 1, 0.0, 0.0, 0.0, 0.0, 0, 103.0, 98.0, 1, 1.0, 0.0, 0, 0, 0, 0, 0, 0, 0.0, 0, 3, 0.0, 0.0, 0, 0, 0.0, 0.0, 0.0, 0, 16.0, 0.0, 0, 0, 2, 0.0, 0.0, 0.0, 0, 0.0, 0.1, 0.05, 0, 0.0, 0, 0.0, 0.0, 0.0, 0, 0, 1, 1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 8, 0, 0, 1, 0, 0)")															   #(9,0,0,10.0,10.0,0.0001,0.0,8.0,0.0,0.0,0.0,1.1,0.0,0.0,100.0,0.9,6,1,1,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0,0,1,0.0,0.0,0.0,1,0.0,0.0,0.0,0.0,0,103.0,98.0,1,1.0,0.0,0,0,0,0,0,0,0.0,0,3,0.0,0.0,0,0,0.0,0.0,0.0,0,16.0,0.0,0,0,2,0.0,0.0,0.0,0,0.0,0.1,0.05,0,0.0,0,0.0,0.0,0.0,0,0,1,1,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0,0,0,8,0,0,1,0,0)
	con.commit()
	con.close()
def Add_Terminal(path_database):
	Max_Element_ID=8
	con = sqlite3.connect(path_database)
	cursorObj = con.cursor()
	# cursorObj.execute("INSERT INTO Terminal VALUES ('13','9','5','1','1','1','0.0','0.0','7','1','0','0','1','0')")
	cursorObj.execute("INSERT INTO Terminal VALUES 	(13, 9, 5, 1, 1, 1, 0.0, 0.0, 7, 1, 0, 0, 1, 0)")
	cursorObj.execute("INSERT INTO Terminal VALUES 	(14, 9, 7, 1, 2, 1, 0.0, 0.0, 7, 1, 0, 0, 1, 0)")
	# cursorObj.execute("INSERT INTO Terminal VALUES (Terminal_ID,Element_ID,Node_ID,'1',Start or end(1 or 2),'1','0.0','0.0','7','1','0','0','1','0')")
	con.commit()
	con.close()
def Add_text(path_database):
	Max_Element_ID=8
	con = sqlite3.connect(path_database)
	cursorObj = con.cursor()
	cursorObj.execute("INSERT INTO GraphicText VALUES (33, 1, 'Arial', 16, 9, 6, 0, 0, 1, 1, 0.0, -2.75e-05, 0.007500000000000001, 1, 0, 0, 1, 1)")
	cursorObj.execute("INSERT INTO GraphicText VALUES (34, 1, 'Arial', 16, 9, 0, 0, 0, 1, 1, 0.0, -2.75e-05, 0.007500000000000001, 1, 0, 0, 1, 1)")
	cursorObj.execute("INSERT INTO GraphicText VALUES (35, 1, 'Arial', 16, 9, 3, 0, 0, 1, 1, 0.0, -2.75e-05, 0.007500000000000001, 1, 0, 0, 1, 1)")
	cursorObj.execute("INSERT INTO GraphicText VALUES (36, 1, 'Arial', 16, 9, 3, 0, 0, 1, 1, 0.0, -2.75e-05, 0.007500000000000001, 1, 0, 0, 1, 1)")
	con.commit()
	con.close()
def Add_GraphicElement(path_database):
	Max_Element_ID=8
	con = sqlite3.connect(path_database)
	cursorObj = con.cursor()	
	cursorObj.execute("INSERT INTO GraphicElement VALUES (9, 1, 1, 36, 0, 9, 16777730, 0, -1, 0, 1, 100, 0.1124925, 0.186750884452884, 20, 0, 0, 1, 1, 1, 0)")
	con.commit()
	con.close()
												#(Graphic_Element_ID, 1, 1,Graphic_text_ID, 0, Element_ID, 16777730, 0, -1, 0, 1, 100, CenterX, CenterY, 20, 0, 0, 1, 1, 1, 0)
def Add_GraphicNode(path_database):
	Max_Element_ID=8
	con = sqlite3.connect(path_database)
	cursorObj = con.cursor()	
	cursorObj.execute("INSERT INTO GraphicNode VALUES (7, 1, 1, 35, 0, 7, 0, -1, 0, 2, 4, 0.1124925, 0.175, 0.1124925, 0.175, 0, 0, 1, 1, 1)")
												     #(GraphicNode_ID, 1, 1,GraphicText_ID, 0, Node_ID, 0, -1, 0, 2, 4, startX, StartY, EndX, EndY, 0, 0, 1, 1, 1)
	con.commit()
	con.close()
def Add_GraphicTerminal(path_database):
	Max_Element_ID=8
	con = sqlite3.connect(path_database)
	cursorObj = con.cursor()	
	cursorObj.execute("INSERT INTO GraphicTerminal VALUES (13, 9, 33, 13,0.1124925, 0.1985025, 0, 0, 1, 0, 4, 20.0, 80, -1, 0, 0, 0, 4, 0.4, 0, -1, 0, 0, 292, 0, 1, 1, 1, 0)")
	cursorObj.execute("INSERT INTO GraphicTerminal VALUES (14, 9, 34, 14,0.1124925, 0.175, 0, 0, 1, 0, 4, 20.0, 80, -1, 0, 0, 0, 4, 0.4, 0, -1, 0, 0, 292, 0, 1, 1, 1, 0)")
					 #Точка присоединения к линии(Graphic_TErminal_ID,GraphicElement_ID,GraphicTExt_ID,Terminal_ID, PosX, PosY, 0, 0, 1, 0, 4, 20.0, 80, -1, 0, 0, 0, 4, 0.4, 0, -1, 0, 0, 292, 0, 1, 1, 1, 0)
	con.commit()
	con.close()
def All(path_database):
	con = sqlite3.connect(path_database)
	dict_Node_ID_U_Un = {}
	dict_Name_Node_ID={}

	cursorObj = con.cursor()
	cursorObj.execute("SELECT * FROM ProtLocation")
	rows = cursorObj.fetchall()
	print(rows)
	con.close()


def Maximum(path_database):# получим имена всех шин, а также найдем максимальный Node_ID
	con = sqlite3.connect(path_database)
	cursorObj = con.cursor()
	Max_Node_ID=cursorObj.execute("SELECT MAX(Node_ID) FROM Node").fetchall()[0][0]#это запрос на самый большой Node_ID в Node
	Max_GraphicText_ID=cursorObj.execute("SELECT MAX(GraphicText_ID) FROM GraphicText").fetchall()[0][0]#это запрос на самый большой GraphicText_ID в GraphicText
	Max_Terminal_ID=cursorObj.execute("SELECT MAX(Terminal_ID) FROM Terminal").fetchall()[0][0]#это запрос на самый большой Terminal_ID в Terminal
	Max_Element_ID=cursorObj.execute("SELECT MAX(Element_ID) FROM Element").fetchall()[0][0]#это запрос на самый большой Element_ID в Element	
	
	ProtLoc_ID=cursorObj.execute("SELECT MAX(ProtLoc_ID) FROM ProtLocation").fetchall()[0][0]
	GraphicAddTerminal_ID=cursorObj.execute("SELECT MAX(GraphicAddTerminal_ID) FROM GraphicAddTerminal").fetchall()[0][0]
	ProtPickup_ID=cursorObj.execute("SELECT MAX(ProtPickup_ID) FROM ProtPickup").fetchall()[0][0]
	ProtSet_ID=cursorObj.execute("SELECT MAX(ProtSet_ID) FROM ProtOCSetting").fetchall()[0][0]

	con.close()
	return Max_Element_ID, Max_Node_ID, Max_Terminal_ID, Max_GraphicText_ID,ProtLoc_ID,GraphicAddTerminal_ID,ProtPickup_ID,ProtSet_ID
def place_trans(TP_Sn,Flag_Lf,path_database,Line_Node_ID,Name,ShortName,PosX,PosY,Max_Element_ID,Max_Node_ID,Max_Terminal_ID,Max_GraphicText_ID,ProtLock_ID,GraphicAddTerminal_ID,ProtPickup_ID,ProtSet_ID):
	con = sqlite3.connect(path_database)
	cursorObj = con.cursor()
	cursorObj.execute("INSERT INTO Element VALUES ({0}, 2, 1, 1, 1, {1}, {2}, 'TwoWindingTransformer', 3, 1, 1, 0, 0, 0.0, 0.0, 0.0, 0.0, 'None', 0.0, 'None', 0.0, 0.0, 0, 0, 0, 0, '', 'None', 1.0, 1.0)".format(str(Max_Element_ID+1),Name,ShortName))
	# cursorObj.execute("INSERT INTO Element VALUES (Element_ID,'2', '1','1', '1','nameTR','ShortNameTR','TwoWindingTransformer','3','1','1','0','0','0.0','0.0','0.0','0.0','NULL','0.0','NULL','0.0','0.0','0','0','0','0','','NULL','1.0','1.0')")#,%Max_Element_ID)
	cursorObj.execute("INSERT INTO Node VALUES ({0}, 1, 1, 2, {1}, {2}, 10.0, 1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, '', 1, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 0, 0, 1, 0.0, 0.0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 'None', 0.0, 'None', 0.0, 0, 0, 0, 0, 0.0, 0.0, 0, 7, 0, 2, 0.0, 0.0, 'None', 0.0, 0)".format(str(Max_Node_ID+1), Name, ShortName))
	# cursorObj.execute("INSERT INTO Node VALUES (Node_ID,'1','1','2','nameNode','ShortNameNode','10.0','1','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0.0','0','1','','1','0','0','0','0','0','0','0','0','0.0','0','0','1','0.0','0.0','0','0','0','0','0.0','0.0','0.0','0.0','NULL','0.0','NULL','0.0','0','0','0','0','0.0','0.0','0','7','0','2','0.0','0.0','NULL','0.0','0')")
	
	cursorObj.execute("INSERT INTO TwoWindingTransformer VALUES ({0}, 67, 1, 10.0, 10.0, 0.0001, 0.0, 8.0, 0.0, 0.0, 0.0, 1.1, 0.0, 0.0, 100.0, 0.9, 6, 1, 1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 1, 0.0, 0.0, 0.0, 1, 0.0, 0.0, 0.0, 0.0, 0, 103.0, 98.0, 1, 1.0, 0.0, 0, 0, 0, 0, 0, 0, 0.0, 0, 3, 0.0, 0.0, 0, 0, 0.0, 0.0, 0.0, 0, 16.0, 0.0, 0, 0, 2, 0.0, 0.0, 0.0, 0, 0.0, 0.1, 0.05, 0, 0.0, 0, 0.0, 0.0, 0.0, 0, 0, 1, 1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 8, 0, 0, 1, 0, 0)".format(str(Max_Element_ID+1)))
													#(Element_ID, 0, 0, 10.0, 10.0, 0.0001, 0.0, 8.0, 0.0, 0.0, 0.0, 1.1, 0.0, 0.0, 100.0, 0.9, 6, 1, 1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 1, 0.0, 0.0, 0.0, 1, 0.0, 0.0, 0.0, 0.0, 0, 103.0, 98.0, 1, 1.0, 0.0, 0, 0, 0, 0, 0, 0, 0.0, 0, 3, 0.0, 0.0, 0, 0, 0.0, 0.0, 0.0, 0, 16.0, 0.0, 0, 0, 2, 0.0, 0.0, 0.0, 0, 0.0, 0.1, 0.05, 0, 0.0, 0, 0.0, 0.0, 0.0, 0, 0, 1, 1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0, 0, 8, 0, 0, 1, 0, 0)
	cursorObj.execute("INSERT INTO Terminal VALUES 	({0}, {1}, {2}, 1, 1, 1, 0.0, 0.0, 7, 1, 0, 0, 1, 0)".format(str(Max_Terminal_ID+1),str(Max_Element_ID+1),str(Line_Node_ID)))
	cursorObj.execute("INSERT INTO Terminal VALUES 	({0}, {1}, {2}, 1, 2, 1, 0.0, 0.0, 7, 1, 0, 0, 1, 0)".format(str(Max_Terminal_ID+2),str(Max_Element_ID+1),str(Max_Node_ID+1)))
	# Terminal_ID,Element_ID,Node_ID,'1',Start or end(1 or 2),'1','0.0','0.0','7','1','0','0','1','0')")
	cursorObj.execute("INSERT INTO GraphicText VALUES ({0}, 1, 'Arial', 16, 9, 6, 0, 0, 1, 1, 0.0, -0.006811, 0.0, 1, 0, 0, 1, 1)".format( str(Max_GraphicText_ID+1)))
	cursorObj.execute("INSERT INTO GraphicText VALUES ({0}, 1, 'Arial', 16, 9, 0, 0, 0, 1, 1, 0.0, -0.00095, -0.00065, 1, 0, 0, 1, 1)".format(str(Max_GraphicText_ID+2)))
	cursorObj.execute("INSERT INTO GraphicText VALUES ({0}, 1, 'Arial', 16, 9, 3, 0, 0, 1, 1, 0.0, -2.75e-05, 0.0075, 1, 0, 0, 1, 1)".format(str(Max_GraphicText_ID+3)))
	cursorObj.execute("INSERT INTO GraphicText VALUES ({0}, 1, 'Arial', 16, 9, 3, 0, 0, 1, 1, 0.0, -2.75e-05, 0.0075, 1, 0, 0, 1, 1)".format(str(Max_GraphicText_ID+4)))
	cursorObj.execute("INSERT INTO GraphicElement VALUES ({0}, 1, 1, {1}, 0,{2}, 16777730, 0, -1, 0, 1, 100, {3},{4}, 20, 0, 0, 1, 1, 1, 0)".format(str(Max_Element_ID+1), str(Max_GraphicText_ID+1), str(Max_Element_ID+1), str(PosX), str(PosY-0.01534)))
														#(Graphic_Element_ID, 1, 1,Graphic_text_ID, 0, Element_ID, 16777730, 0, -1, 0, 1, 100, CenterX, CenterY, 20, 0, 0, 1, 1, 1, 0)
	cursorObj.execute("INSERT INTO GraphicNode VALUES ({0}, 1, 1, {1}, 0, {2}, 0, -1, 0, 2, 4, {3}, {4}, {5}, {6}, 0, 0, 1, 1, 1)".format (str(Max_Node_ID+1), str(Max_GraphicText_ID+2), str(Max_Node_ID+1), str(PosX), str(PosY-0.02436), str(PosX), str(PosY-0.02436)))
												     #(GraphicNode_ID, 1, 1,GraphicText_ID, 0, Node_ID, 0, -1, 0, 2, 4, startX, StartY, EndX, EndY, 0, 0, 1, 1, 1)
	cursorObj.execute("INSERT INTO GraphicTerminal VALUES ({0}, {1}, {2}, {3},{4}, {5}, 0, 0, 1, 0, 4, 20.0, 80, -1, 0, 0, 0, 4, 0.4, 0, -1, 0, 0, 292, 0, 1, 1, 1, 0)".format(str(Max_Terminal_ID+1), str(Max_Element_ID+1),str(Max_GraphicText_ID+3), str(Max_Terminal_ID+1), str(PosX), str(PosY)))
	cursorObj.execute("INSERT INTO GraphicTerminal VALUES ({0}, {1}, {2}, {3},{4}, {5}, 0, 0, 1, 0, 4, 20.0, 80, -1, 0, 0, 0, 4, 0.4, 0, -1, 0, 0, 292, 0, 1, 1, 1, 0)".format(str(Max_Terminal_ID+2), str(Max_Element_ID+1),str(Max_GraphicText_ID+4),str(Max_Terminal_ID+2),str(PosX), str(PosY-0.02436)))
					 #Точка присоединения к линии(Graphic_TErminal_ID,GraphicElement_ID,GraphicTExt_ID,Terminal_ID, PosX, PosY, 0, 0, 1, 0, 4, 20.0, 80, -1, 0, 0, 0, 4, 0.4, 0, -1, 0, 0, 292, 0, 1, 1, 1, 0)
	
	#отрисовка нагрузки
	cursorObj.execute("INSERT INTO Element VALUES ({0}, 2, 1, 1, 1,{1}, {2}, 'Load', 3, 1, 1, 0, 0, 0.0, 0.0, 0.0, 0.0, 'None', 0.0, 'None', 0.0, 0.0, 0, 0, 0, 0, '', 'None', 1.0, 1.0)".format(str(Max_Element_ID+2),Name,ShortName))
	# cursorObj.execute("INSERT INTO Element VALUES (Element_ID,'2', '1','1', '1','nameTR','ShortNameTR','TwoWindingTransformer','3','1','1','0','0','0.0','0.0','0.0','0.0','NULL','0.0','NULL','0.0','0.0','0','0','0','0','','NULL','1.0','1.0')")#,%Max_Element_ID)
	cursorObj.execute("INSERT INTO Load VALUES ({0}, 0, 1, 2, {1}, 0.0, 0.0, {2}, {3}, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1, 0, 0, 0, 0, 1, 1, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1, 1.0, 0.0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.95, 1, 0.0, 0.75, 0, 0, 0, 1, 1, 0.0, 0.0, 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, 0.0, 0.0, 0.0, 0.0)".format(str(Max_Element_ID+2),str(Flag_Lf),"'"+str(TP_Sn.get(Name.replace("'","")))+"'","'"+str(TP_Sn.get(Name.replace("'","")))+"'"))
	print(Name.replace("'",""))
	cursorObj.execute("INSERT INTO Terminal VALUES 	({0}, {1}, {2}, 1, 1, 1, 0.0, 0.0, 7, 1, 0, 0, 1, 0)".format(str(Max_Terminal_ID+3),str(Max_Element_ID+2),str(Max_Node_ID+1)))
	# cursorObj.execute("INSERT INTO Terminal VALUES (Terminal_ID,Element_ID,Node_ID,'1',Start or end(1 or 2),'1','0.0','0.0','7','1','0','0','1','0')")
	cursorObj.execute("INSERT INTO GraphicElement VALUES ({0}, 1, 1, {1}, 0, {2}, 1, 0, -1, 0, 1, 100, {3}, {4}, 13, 0, 0, 1, 1, 1, 0)".format(str(Max_Element_ID+2), str(Max_GraphicText_ID+5), str(Max_Element_ID+2), str(PosX), str(PosY-0.02753)))
														#(Graphic_Element_ID, 1, 1,Graphic_text_ID, 0, Element_ID, 16777730, 0, -1, 0, 1, 100, CenterX, CenterY, 20, 0, 0, 1, 1, 1, 0)
	cursorObj.execute("INSERT INTO GraphicTerminal VALUES ({0}, {1}, {2}, {3}, {4}, {5}, 0, 0, 1, 0, 4, 20.0, 80, -1, 0, 0, 0, 4, 0.4, 0, -1, 0, 0, 292, 0, 1, 1, 1, 0)".format(str(Max_Terminal_ID+3), str(Max_Element_ID+2),str(Max_GraphicText_ID+6), str(Max_Terminal_ID+3), str(PosX), str(PosY-0.02436)))
					 #Точка присоединения к линии(Graphic_TErminal_ID,GraphicElement_ID,GraphicTExt_ID,Terminal_ID, PosX, PosY, 0, 0, 1, 0, 4, 20.0, 80, -1, 0, 0, 0, 4, 0.4, 0, -1, 0, 0, 292, 0, 1, 1, 1, 0)
	cursorObj.execute("INSERT INTO GraphicText VALUES ({0}, 1, 'Arial', 16, 9, 6, 0, 0, 1, 1, 0.0,0.0, -0.0075,  1, 0, 0, 1, 1)".format( str(Max_GraphicText_ID+5)))
	cursorObj.execute("INSERT INTO GraphicText VALUES ({0}, 1, 'Arial', 16, 9, 0, 0, 0, 1, 1, 0.0, -2.75e-05, 0.0075, 1, 0, 0, 1, 1)".format( str(Max_GraphicText_ID+6)))
	
	#Настройка защиты(предохранителя)


	#GraphicAddTerminal
	cursorObj.execute("INSERT INTO GraphicAddTerminal VALUES ({0}, {1}, 1, 1, {2}, 0, -1, 0, 1, 80, 1, 4, 0, {3}, {4}, 292, 2048, 2, 86, 1, 0, {5}, 1, 1)".format(str(GraphicAddTerminal_ID+1),str(Max_Terminal_ID+1),str(Max_GraphicText_ID+7),str(0.0),str(-0.0),str(20.0)))
	#(GraphicAddTerminal_ID, GraphicTerminal_ID, 1, 1, GraphicText_ID, 0, -1, 0, 1, 80, 1, 4, 0, PosX, PosY, 292, 2048, 2, 86, 1, 0, SymNodePos(Расстояние до узла), 1, 1)
	#ProtPickup
	cursorObj.execute("INSERT INTO ProtPickup VALUES ({0}, {1}, 2, 0, 0, 0.0, 0, 0, 0.0, 0, 0.0, 0.0, 0, 0.0, 0.0, 0, 0.0, 0.0, 0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0, 1.0, 1.0, 1.5, 1.2, 0.7, 1.0, 30.0, 0.0, 0, 1.0, 1.0, 1.5, 1.2, 0.7, 1.0, 30.0, 0.0, 1, 1, 0.0, 90.0, 0.0, 90.0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)".format(str(ProtPickup_ID+1),str(ProtLock_ID+1)))
	#(ProtPickup_ID, ProtLock_ID, 2, 0, 0, 0.0, 0, 0, 0.0, 0, 0.0, 0.0, 0, 0.0, 0.0, 0, 0.0, 0.0, 0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0, 0.0, 0.0, 0.0, 0, 1.0, 1.0, 1.5, 1.2, 0.7, 1.0, 30.0, 0.0, 0, 1.0, 1.0, 1.5, 1.2, 0.7, 1.0, 30.0, 0.0, 1, 1, 0.0, 90.0, 0.0, 90.0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0)
	#ProtOCSetting
	cursorObj.execute("INSERT INTO ProtOCSetting VALUES ({0}, {1}, 2287, 2287,'HH-SE (80 A)','HH-SE (80 A)', 0.0, 1.8, 0.0, 0.0, 0.0, 80.0, 0, 135.0, 315.0, -45.0, 135.0, 1, 0.0, 0.0, 0, 135.0, 315.0, -45.0, 135.0, 1, 0, 1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0.0, 0.0, 0.0, 0.0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1, 0.0, 4, 1, 0.0, 1, 0, 0.0, 1, 1, 0, 1, 0.0, 4, 1, 0.0, 1, 0, 0.0, 1, 1, 0, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 4, 0, 0.0, 4)".format(str(ProtSet_ID+1),str(ProtLock_ID+1)))
	#(ProtSet_ID, ProtLock_ID, ProtCharP_ID(2287), ProtCharE_ID(2287), p_nam('HH-SE (80 A)'),e_nam('HH-SE (80 A)'), 0.0, 1.8, 0.0, 0.0, 0.0, 80.0, 0, 135.0, 315.0, -45.0, 135.0, 1, 0.0, 0.0, 0, 135.0, 315.0, -45.0, 135.0, 1, 0, 1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, 1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 9, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0.0, 0.0, 0.0, 0.0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1, 0.0, 4, 1, 0.0, 1, 0, 0.0, 1, 1, 0, 1, 0.0, 4, 1, 0.0, 1, 0, 0.0, 1, 1, 0, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.0, 4, 0, 0.0, 4)
	#ProtMinMax
	cursorObj.execute("INSERT INTO ProtMinMax VALUES ({0}, {1}, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1)".format(str(ProtSet_ID+1),str(ProtLock_ID+1)))
	#(ProtSet_ID, ProtLock_ID, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1)
	#ProtLocation
	cursorObj.execute("INSERT INTO ProtLocation VALUES ({0}, 825, 0, {1}, 0, 1, {2}, 1, 0, 0, 0, 0, 0, 0, 0.0, 1, 1, 2, 0.0, 0.0, 0.0, 0.0, 1, 1, 1, 135.0, -45.0, 315.0, 135.0, 1, 135.0, -45.0, 315.0, 135.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 0, '', 0.0, 0, 0, 0, 0, 0, 'None', 0.0, 0.0, 0, 0, 0, 0, 0, 0, 0.0)".format(str(ProtLock_ID+1),str(Max_Terminal_ID+1),Name))
	#(ProtLock_ID, ProtDev_ID(825), 0, Terminal_ID(Трансформатора), Node_ID(0), 1, Name, 1, 0, 0, 0, 0, 0, 0, 0.0, 1, 1, 2, 0.0, 0.0, 0.0, 0.0, 1, 1, 1, 135.0, -45.0, 315.0, 135.0, 1, 135.0, -45.0, 315.0, 135.0, 1, 1, 0.0, 0.0, 0.0, 0.0, 0, '', 0.0, 0, 0, 0, 0, 0, None, 0.0, 0.0, 0, 0, 0, 0, 0, 0, 0.0)
	cursorObj.execute("INSERT INTO GraphicText VALUES ({0}, 1, 'Arial', 16, 9, 0, 0, 0, 1, 1, 0.0, 0.03, -0.015, 1, 0, 0, 1, 1)".format( str(Max_GraphicText_ID+7)))
	
	con.commit()
	con.close()
def Get_Bus_data(path_database,Line_Node_ID):
	con = sqlite3.connect(path_database)
	cursorObj = con.cursor()
	cursorObj.execute("SELECT NodeStartX, NodeStartY, NodeEndX FROM GraphicNode WHERE Node_ID='{0}'".format(str(Line_Node_ID)))
	rows = cursorObj.fetchall()
	PosX=(rows[0][0]+rows[0][2])/2
	PosY=rows[0][1]
	con.close()
	return PosX,PosY
def place_elements(TP_Sn,Flag_Lf):
	con = sqlite3.connect(path_database)
	cursorObj = con.cursor()
	Node_ID_Name = []
	cursorObj.execute("SELECT  Name, Node_ID  FROM Node WHERE Flag_Type=2")
	rows = cursorObj.fetchall()
	for row in rows:
		Node_ID_Name.append((row[1],row[0]))

	for Node_ID in Node_ID_Name:
		Position=Get_Bus_data(path_database,Node_ID[0])
		PosX=Position[0]
		PosY=Position[1]

		Maximums=Maximum(path_database)
		if Maximums[0]==None :
			Max_Element_ID=0
		else:
			Max_Element_ID=Maximums[0]
		if Maximums[1]==None :
			Max_Node_ID=0
		else:
			Max_Node_ID=Maximums[1]
		if Maximums[2]==None :
			Max_Terminal_ID=0
		else:
			Max_Terminal_ID=Maximums[2]
		if Maximums[3]==None :
			Max_GraphicText_ID=0
		else:
			Max_GraphicText_ID=Maximums[3]
		if Maximums[4]==None :
			ProtLoc_ID=0
		else:
			ProtLoc_ID=Maximums[4]
		if Maximums[5]==None:
			GraphicAddTerminal_ID=0
		else:
			GraphicAddTerminal_ID=Maximums[5]
		if Maximums[6]==None:
			ProtPickup_ID=0
		else:
			ProtPickup_ID=Maximums[6]
		if Maximums[7]==None:
			ProtSet_ID=0
		else:
			ProtSet_ID=Maximums[7]

		place_trans(TP_Sn,Flag_Lf,path_database,Node_ID[0],"'{0}'".format(Node_ID[1]),"'{0}'".format(Node_ID[1]),PosX,PosY,Max_Element_ID, Max_Node_ID, Max_Terminal_ID, Max_GraphicText_ID,ProtLoc_ID,GraphicAddTerminal_ID,ProtPickup_ID,ProtSet_ID)
	con.close()
def get_Sn():
	TP_Sn={}
	csv_path = "LoadPower.csv"
	tables = pd.read_csv(csv_path, sep=';',encoding="utf_8")
	print(tables)
	for i in range(len(list(tables['ТП']))):
		TP_Sn[str(list(tables['ТП'])[i])]=float(list(tables['Sнагр'])[i].replace(",",'.'))
	print(TP_Sn)
	return(TP_Sn)
	
TP_Sn=get_Sn()
place_elements(TP_Sn,4)