import random

# ---------------------------------------------------------------
#     MyCompany クラス
# ---------------------------------------------------------------
class MyCompany():
	def __init__( self ):
		print();  print("MyCompanyのオブジェクト生成完了");  print()















	def setInfoData( self, employeenum ):
		self.EmployeeNum = employeenum
		self.InfoList = []
		for nn in range( 1, employeenum + 1 ):
			ID = "";  Age = 0;  Job= "";  Grade = ""
			# =====  ID  ======
			if   nn<10:     ID = "id_00"+str(nn)
			elif nn<100:    ID = "id_0" +str(nn)
			else:           ID = "id_"  +str(nn)

			# =====  年齢  ======
			Age = random.randrange( 18, 65)

			# =====  職種  ======
			x = random.randrange( 1, 101)
			if   x<10:    Job= "事務"
			elif x<40:    Job= "営業"
			else:         Job= "技術"

			# =====  Grade  ======
			y = random.randrange( 1, 101)
			if   y<12:    Grade = "A"
			elif y<42:    Grade = "B"
			elif y<92:    Grade = "C"
			elif y<97:    Grade = "D"
			else:         Grade = "E"
			self.InfoList.append( [ID,Age,Job,Grade] )
		print("社員の情報作成完了");  print()


	def getInfoData( self ):
		return self.InfoList





	def Evaluation( self ):
		EvaList = [[0,0],[0,0],[0,0]]
		for row in self.InfoList:
			if   row[2]=="事務" and row[3]=="A":  EvaList[0][0] += 1
			elif row[2]=="事務" and row[3]=="B":  EvaList[0][1] += 1
			elif row[2]=="営業" and row[3]=="A":  EvaList[1][0] += 1
			elif row[2]=="営業" and row[3]=="B":  EvaList[1][1] += 1
			elif row[2]=="技術" and row[3]=="A":  EvaList[2][0] += 1
			elif row[2]=="技術" and row[3]=="B":  EvaList[2][1] += 1
		return EvaList








# ---------------------------------------------------------------
#     オブジェクト(company)の生成 と メソッド呼び出し操作
# ---------------------------------------------------------------
company = MyCompany()
company.setInfoData( 100 )
RetList = company.getInfoData()
for row in RetList:    print(row)
RetEva = company.Evaluation()
print()
for row in RetEva: print(row)
