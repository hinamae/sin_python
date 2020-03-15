# 課題 FirstQClass11.py
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
		ans = hankei*hankei*np.pi
		print("円の面積＝(%7.3f)" %ans )

	def Shikaku(self, tate, yoko ): #長方形：縦ｘ横
		ans = tate*yoko
		print("長方形の面積＝(%7.2f)" %ans )

	def Sankaku(self, teihen, takasa ): #三角形：底辺ｘ高さ
		ans = teihen*takasa/2
		print("三角形の面積＝(%7.2f)" %ans )

# ★★★★★★★★★★★★★★★★★★★★★★★★

print()
area = AreaClass()
print(area)

area.En(10)
area.Shikaku(4, 5)
area.Sankaku(4, 10)




# ◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆
