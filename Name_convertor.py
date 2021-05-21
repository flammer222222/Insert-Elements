class Convertor:
	def name_convertor(name,element_type):
		NameTrLd=[('Т','Т-1','Т-2'),('H','H-1','H-2'),('З','З-1','З-2')]
		if str(name).strip().replace('1C','С1').replace('1С','С1').replace('C1','С1').find('С1')!=-1:
			return str(name).replace('1C','С1').replace('1С','С1').replace('C1','С1').replace('С1',NameTrLd[element_type][1])# махинации, чтобы читать С и русскую, и английску C
		elif str(name).strip().replace('2C','С2').replace('2С','С2').replace('C2','С2').find('С2')!=-1:
			return str(name).strip().replace('2C','С2').replace('2С','С2').replace('C2','С2').replace('С2',NameTrLd[element_type][2])
		else:
			return str(name).strip()+" "+NameTrLd[element_type][0]

if __name__ == "__main__":
	Name=Convertor.name_convertor("ТП-2231 C2",1)
	print(Name)