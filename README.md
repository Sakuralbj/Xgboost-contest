# xgboostReadme
  #                      说明文件



## 1运行环境

 python3.6  sklearn

## 2程序结构

Data文件夹存放所有数据，data.raw存放原始数据，log.txt存放每个属性各个数字代表的意义，map.txt代表log.txt转换后的格式，Alldata.txt数据处理后的输入数据。Testdata和train data分别代表测试和训练数据，数据格式调整好后，Xgboost进行训练，训练的结果保存在Result里面。

## 3.代码说明

运行change map.py将log.txt格式转换为map.txt，map feat.py根据map.txt将data.raw转换为输入数据Alldata.txt,mknfold.py把所有的输入数据划分到Testdata和Traindata里，然后运行Xgboost.py将最后的概率结果保存到Result.txt里面。

## 4.输入输入格式

#### 输入：

##### 原始数据：

```
1,0,1,11,1,0,1
1,0,1,11,1,1,1
1,1,-8,11,1,1,1
```

第一列代表标签，后面的数字代表某个属性。

##### 转换后的数据：

```
1 5:1 20:1 26:1 63:1 69:1 78:1
```

第一个代表标签，后面的冒号前面的数字代表该数据第几个属性出现过。

输出：输出为一个小数，代表其值的预测概率。


