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

	def En(self, hankei):               #円：半径ｘ半径ｘパイ
		ans = hankei*hankei*np.pi
		return ans
	def Shikaku(self, tate, yoko ):     #長方形：縦ｘ横
		ans = tate*yoko
		return ans
	def Sankaku(self, teihen, takasa ): #三角形：底辺ｘ高さ
		ans = teihen*takasa/2
		return ans
# ★★★★★★★★★★★★★★★★★★★★★★★★
class Area_Capacity_Class( AreaClass ):
    # --------体積：volume、capacity
	def TyokuhouTai(self, tate, yoko, takasa):        #直方体：底面積(長方形)ｘ高さ
		ans = (tate*yoko)*takasa
		print(ans)
	def SankakuSui(self, teihen, teiTakasa, takasa): #三角錐：底面積(3角形)ｘ高さ/３
		ans = (teihen*teiTakasa/2)*takasa
		print(ans)
	def EnTyu(self, hankei, takasa ):                #円柱：底面積（円）ｘ高さ
		ans = (hankei*hankei*np.pi)*takasa
		print(ans)
	def KyuTai(self, hankei):                        #球：sphere (4/3)ｘパイｘ半径^3
		ans = (4*np.pi*hankei*hankei*hankei)/3
		print(ans)
# ★★★★★★★★★★★★★★★★★★★★★★★★

print()
area = AreaClass()
print(area)

print( area.En(10) )
print( area.Shikaku(4, 5) )
print( area.Sankaku(4, 10) )

areaCapacity = Area_Capacity_Class()
areaCapacity.TyokuhouTai(4, 5, 10)
areaCapacity.SankakuSui(4, 5, 10 )
areaCapacity.EnTyu( 10, 10 )
areaCapacity.KyuTai( 10 )

# ◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆
