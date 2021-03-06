# 課題 FirstQClass33.py
import numpy as np
import math

# ★★★★★★★★★★★★★★★★★★★★★★★★
class AreaClass:
	def __init__(self):
		print("ー＞")
		pass
	def __str__(self):
		return "クラス名=AreClass(面積)"
	def __del__(self):
		print("+++++解放+++++")


	def Circle(self, hankei): #円：半径ｘ半径ｘパイ
		return hankei*hankei*math.pi
		pass

	def Square(self, tate, yoko): #長方形：縦ｘ横
		return tate*yoko
		pass


	def Triangle(self, teihen, takasa): #三角形：底辺ｘ高さ/2
		return teihen*takasa*0.5
		pass

# ★★★★★★★★★★★★★★★★★★★★★★★★
class Area_Capacity_Class(AreaClass):
    # --------体積：volume、capacity
	def TyokuhouTai(self, tate, yoko, takasa ): #直方体：底面積(長方形)ｘ高さ
		area=AreaClass()
		menseki=area.Square(tate,yoko)
		return print(menseki*takasa)
		pass

	def SankakuSui(self, teihen, teiTakasa, takasa): #三角錐：底面積(3角形)ｘ高さ/３
		area=AreaClass()
		menseki=area.Triangle(teihen,teiTakasa)
		return print(menseki*takasa*1/3)
		pass

	def EnTyu(self, hankei, takasa): #円柱：底面積（円）ｘ高さ
		area=AreaClass()
		menseki=area.Circle(hankei)
		return print(menseki*takasa)
		pass

	def KyuTai(self, hankei): #球：sphere (4/3)ｘパイｘ半径^3
		area=AreaClass()
		menseki=area.Circle(hankei)
		return print(menseki*math.pi*4/3)
		pass

# ★★★★★★★★★★★★★★★★★★★★★★★★

# ◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆


# コンストラクタの生成
area = Area_Capacity_Class()
# メソッド使用
print("直方体の体積")
area.TyokuhouTai(4,5,10)
print("三角錐の体積")
area.SankakuSui(4,5,10)
print("円柱の体積")
area.EnTyu(10,10)
print("球体の体積")
area.KyuTai(10)
