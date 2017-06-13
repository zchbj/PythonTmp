#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from pylab import rcParams
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
rcParams['font.sans-serif'] = ['Songti']  # 指定默认字体
rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
rcParams["pdf.fonttype"] = 42

from matplotlib.font_manager import FontProperties
font=FontProperties(fname=r'/Library/fonts/Songti.ttc',size=14) # mac下的路径

np.random.seed(1000)
y = np.random.standard_normal(20)

x = range(len(y))
print x
plt.plot(x,y)
plt.xlabel('X轴'.decode('utf'), fontproperties=font) # 必须指定font 否则保存后无法显示中文
plt.ylabel(u'Y轴', fontproperties=font)
plt.savefig('plt.pdf')
plt.show()


