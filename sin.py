
import numpy as np
import matplotlib.pyplot as plt # pltとしてインポートされるのが慣例です。
X = np.linspace(-10, 10, 1000)   # 1000個がない場合は50個
y = np.sin(X) # サインの値を計算する
plt.plot(X, y) # これでプロットをする。plotで点と点同⼠をなめらかにつなぐ
plt.show() # グラフの表⽰
