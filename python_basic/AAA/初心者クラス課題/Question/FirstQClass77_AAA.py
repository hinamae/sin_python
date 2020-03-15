# 課題 FirstQ22_AAA.py
import numpy as np

def ReadBaseBallPlayer():
	Data00 = []
	fp = open('BaseBallPlayer.dat', "r", encoding='utf-8')
	nn = 0
	for row in fp:
		if nn != 0:
			Data00.append( row.replace( "\n", "") )
		nn = 1
	fp.close()

	Data0 = []
	index00 = np.array( range(0, len(Data00)) )
	np.random.shuffle( index00 )
	for nn in index00:
		Data0.append( Data00[nn] )
	return Data0
# ★★★★★★★★★★★★★★★★★★★★★★★★
