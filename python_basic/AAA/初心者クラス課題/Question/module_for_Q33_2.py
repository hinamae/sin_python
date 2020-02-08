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
