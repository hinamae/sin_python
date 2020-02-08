# 課題 FirstQClass00.py
import numpy as np
import math

# ★★★★★★★★★★★★★★★★★★★★★★★★
class AreaClass:
	def __init__(self):
		print("+++++面積+++++")
		pass
	def __str__(self):
		return "クラス名=AreClass(面積)"
	def __del__(self):
		print("+++++解放+++++")


	def Circle(self, hankei): #円：半径ｘ半径ｘパイ
		print(hankei*hankei*math.pi)
		pass

	def Square(self, tate, yoko): #長方形：縦ｘ横
		print(tate*yoko)
		pass


	def Triangle(self, teihen, takasa): #三角形：底辺ｘ高さ/2
		print(teihen*takasa*0.5)
		pass

class Question:
	def __init__(self):
		print("+++++数値の入力+++++")
		pass
	def __str__(self):
		return "クラス名=Question（質問）"
	def __del__(self):
		print("+++++解放+++++")

	def Que_C(self):
		print("円の半径を入力してください")
		return float(input())
	def Que_S(self):
		print("長方形の縦の長さを入力してください")
		tate=float(input())
		print("長方形の横の長さを入力してください")
		yoko=float(input())
		# ,でくぎられたデータはタプルとなる
		return tate, yoko
	def Que_T(self):
		print("三角形の底辺の長さを入力してください")
		teihen=float(input())
		print("三角形の高さを入力してください")
		takasa=float(input())
		# ,でくぎられたデータはタプルとなる
		return teihen, takasa

	

# ★★★★★★★★★★★★★★★★★★★★★★★★



# ◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆
que = Question()
hankei_C = que.Que_C()
tateyoko_S = que.Que_S()
teihentakasa_T = que.Que_T()
# コンストラクタの生成
area = AreaClass()
# 円メソッド使用
area.Circle(hankei_C)
area.Square(tateyoko_S[0],tateyoko_S[1])
area.Triangle(teihentakasa_T[0],teihentakasa_T[1])