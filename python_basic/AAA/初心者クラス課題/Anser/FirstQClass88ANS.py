# 課題 FirstQClass88.py   ( FirstQClass77_AAA.py    BaseBallPlayer.dat )

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
		self.Data00 = []
		for row in self.Data0:        #  row <==  "柳田選手,316,7,ソフトバンク"
			list0 = row.split( "," )
			list0[1] = int( list0[1] )
			list0[2] = int( list0[2] )
			self.Data00.append( list0 )

	def HitRatio(self):
		# ++++名前[0]  reverse = False
		self.Data00.sort(key=lambda x:x[0] )
		# ++++打率[1]  reverse = True
		print("++++++++++++++++++++++打   率++++++++++++++++++++++")
		self.Data00.sort(key=lambda x:x[1], reverse = True )
		count = 0
		nn = -1
		mm = 0
		for row in self.Data00:
			if nn != row[1]:
				nn = row[1]
				mm += 1
				count += 1
				if count== 4 or mm >= 4:
					break
				print( row )
			else:
				mm += 1
				print( row )

	def HomeRun(self):
		# ++++ホームラン[2]  reverse = True
		print("++++++++++++++++++++++ホームラン++++++++++++++++++++++")
		self.Data00.sort(key=lambda x:x[2], reverse = True )

		count = 0
		nn = -1
		mm = 0
		for row in self.Data00:
			if nn != row[2]:
				nn = row[2]
				mm += 1
				count += 1
				if count== 4 or mm >= 4:
					break
				print( row )
		else:
			mm += 1
			print( row )
# ★★★★★★★★★★★★★★★★★★★★★★★★


#str = ReadBaseBallPlayer
print()
player = Player_00( )
print(player)


print()
print("データ作成")
player.Make2D_Data()

print()
print("打率")
player.HitRatio()

print()
print("ホームラン")
player.HomeRun()

print();  print();  print("プログラム修了");  print(); print()
# ◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆◆
