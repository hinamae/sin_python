# coding: UTF-8
import random
import math

class MyCompany:
    def __init__(self):
        print("MyCompanyのオブジェクト生成完了")
        pass
    def __str__(self):
        return "クラス名=AreClass(面積)"
    def __del__(self):
        print("+++++解放+++++")

    def setInfoData(self,employeenum):
        # インスタンス変数を定義(インスタンス変数=このクラスから生成されたオブジェクトが持つ変数)
        self.EmployeeNum = employeenum
        self.InfoList = []
         
        id=1
        for num in range(employeenum):
            # idについて
            if id < 100 :
                id_str="ID_00"+str(id)
            elif id < 1000:
                id_str="ID_0"+str(id)
            else:
                print("人数超過")
            print("IDは"+str(id_str))
            id=id+1

            # 年齢について
            age=random.randrange(18,64)
            print("歳は"+str(age))

            # 職種について
            flag_job=random.randrange(0,100)
            if flag_job >= 0 and flag_job <= 9:
                job='事務'
            elif flag_job >= 10 and flag_job <= 39:
                job='営業'
            else:
                job='技術'
            print("jobは"+job)

            # 評価について
            flag_eval=random.randrange(0,100)
            if flag_eval >= 0 and flag_eval <= 2:
                evaluation="A"
            elif flag_eval >= 3 and flag_eval <= 7:
                evaluation="B"
            elif flag_eval >= 8 and flag_eval <= 57:
                evaluation="C"
            elif flag_eval >= 58 and flag_eval <= 87:
                evaluation="D"
            else:
                evaluation="E"
            print("評価は"+evaluation)

            # 情報をインスタンス変数に格納(listをappend)
            self.InfoList.append([id_str,age,job,evaluation])
            
        # infoList=
        print("社員の情報作成完了")

    def getInfoData(self):
        return self.InfoList

    def Evaluation(self):
        count_jimu_A=0
        count_jimu_B=0

        count_eigyo_A=0
        count_eigyo_B=0
        
        count_gijyutu_A=0
        count_gijyutu_B=0

        EvaList=[]
        # あとで関数にする
        for li in self.InfoList:
            if str(li[2])=="事務" and str(li[3])=="A":
                count_jimu_A=count_jimu_A+1
            
            if str(li[2])=="事務" and str(li[3])=="B":
                count_jimu_B=count_jimu_B+1
            
            
            if str(li[2])=="営業" and str(li[3])=="A":
                count_eigyo_A=count_eigyo_A+1
            
            
            if str(li[2])=="営業" and str(li[3])=="B":
                count_eigyo_B=count_eigyo_B+1

                
            if str(li[2])=="技術" and str(li[3])=="A":
                count_gijyutu_A=count_gijyutu_A+1
                
            if str(li[2])=="技術" and str(li[3])=="B":
                count_gijyutu_B=count_gijyutu_B+1
        EvaList=[[count_jimu_A,count_jimu_B],[count_eigyo_A,count_eigyo_B],[count_gijyutu_A,count_gijyutu_B]]
        return EvaList
# ---------------------------------------------------------------
#     オブジェクト(company)の生成 と メソッド呼び出し操作
# ---------------------------------------------------------------

company=MyCompany()
company.setInfoData(100)
RetList=company.getInfoData()
# 全員分のデータを表示
for li in RetList:
    print(str(li[0])+","+str(li[1])+","+str(li[2])+","+str(li[3]))

RetEva=company.Evaluation()
print(RetEva)
