# 課題 FirstQClass77.py   ( FirstQClass77_AAA.py    BaseBallPlayer.dat )

from FirstQClass77_AAA import ReadBaseBallPlayer as ReadBaseBallPlayer

# ★★★★★★★★★★★★★★★★★★★★★★★★
class Player_00:
	def __init__(self):
		print("++++++++++コンストラクタが呼び出された++++++++++")
		self.Data0 = ReadBaseBallPlayer()
		print(); print()

	def __str__(self):
		return "++++++++++クラス名=Player_00++++++++++"

	def __del__(self):
		print("++++++++++オブジェクト:Playerの解放++++++++++")

	def Make2D_Data(self):
		# ++++++++++設問１++++++++++
		pass
	def HitRatio(self):
		# ++++++++++++++++++++++打   率++++++++++++++++++++++
		pass
	def HomeRun(self):
		# ++++++++++++++++++++++ホームラン++++++++++++++++++++++
		pass
# ★★★★★★★★★★★★★★★★★★★★★★★★


# ◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆
