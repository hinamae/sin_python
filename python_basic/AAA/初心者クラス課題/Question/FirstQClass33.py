# 課題 FirstQClass33.py
import numpy as np

# ★★★★★★★★★★★★★★★★★★★★★★★★
class AreaClass:
	def __init__(self):
		print("+++++コンストラクタ+++++")
		pass
	def __str__(self):
		return "クラス名=AreClass(面積)"
	def __del__(self):
		print("+++++解放+++++")

	def En(self, hankei): #円：半径ｘ半径ｘパイ
		pass

	def Shikaku(self, tate, yoko ): #長方形：縦ｘ横
		pass

	def Sankaku(self, teihen, takasa ): #三角形：底辺ｘ高さ/2
		pass

# ★★★★★★★★★★★★★★★★★★★★★★★★
class Area_Capacity_Class:
    # --------体積：volume、capacity
	def TyokuhouTai(self, tate, yoko, takasa ): #直方体：底面積(長方形)ｘ高さ
		pass

	def SankakuSui(self, teihen, teiTakasa, takasa): #三角錐：底面積(3角形)ｘ高さ/３
		pass

	def EnTyu(self, hankei, takasa): #円柱：底面積（円）ｘ高さ
		pass

	def KyuTai(self, hankei): #球：sphere (4/3)ｘパイｘ半径^3
		pass

# ★★★★★★★★★★★★★★★★★★★★★★★★

# ◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆
