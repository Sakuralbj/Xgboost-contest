# -*- coding: utf-8 -*-
#!/usr/bin/python
# 将数据随机分为训练集和测试集

import random

fi = open( "../Data/Alldata2014.txt", 'r' )
ftrain = open( '../Data/Traindata2014.txt', 'w' )
ftest = open( '../Data/Testdata2014.txt', 'w' )
for line in fi:
    if random.randint( 1 , 10 ) <= 2:
        ftest.write( line )
    else:
        ftrain.write( line )

fi.close()
ftrain.close()
ftest.close()
