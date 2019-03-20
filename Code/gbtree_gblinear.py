# -*- coding: utf-8 -*-
# 训练模型输出结果
# 需导入xgboost库

import xgboost as xgb

dtrain = xgb.DMatrix('../Data/Traindata2014.txt')
dtest = xgb.DMatrix('../Data/Testdata2014.txt')
test_y = dtest.get_label()
# 以CART回归树作为基学习器
params_gbtree={'booster':'gbtree',
    'objective': 'reg:linear',
    'eval_metric': 'auc',
    'scale_pos_weight':'1',
    'max_depth':6,
    'lambda':2,
    'subsample':0.75,
    'colsample_bytree':0.75,
    'min_child_weight':1,
    'eta': 0.025,
    'seed':0,
    'nthread':8,
     'silent':1}

watchlist = [(dtrain,'train')]

bst_gbtree=xgb.train(params_gbtree,dtrain,num_boost_round=300,evals=watchlist)

# 以线性分类器作为基学习器
params={'booster':'gblinear',
    'objective': 'reg:linear',
    'eval_metric': 'auc',
    'scale_pos_weight':'10',
    'lambda':2,
    'eta': 0.025,
    'seed':0,
    'nthread':8,
     'silent':1}

watchlist = [(dtrain,'train')]

bst_gblinear=xgb.train(params,dtrain,num_boost_round=200,evals=watchlist)

# 模型融合
y_pred_gblinear=bst_gblinear.predict(dtest)
y_pred_gbtree=bst_gbtree.predict(dtest)
y_pred = 0.3*y_pred_gblinear+0.7*y_pred_gbtree
from sklearn import metrics
print('test_AUC_gblinear: %.4f' % metrics.roc_auc_score(test_y,y_pred_gblinear))
print('test_AUC_gbtree: %.4f' % metrics.roc_auc_score(test_y,y_pred_gbtree))
print('test_AUC: %.4f' % metrics.roc_auc_score(test_y,y_pred))

# ROC曲线
from matplotlib import pyplot as plt
fpr_1, tpr_1, thresholds_1=metrics.roc_curve(test_y,y_pred_gblinear,pos_label=1,sample_weight=None,drop_intermediate=True)
fpr_2, tpr_2, thresholds_2=metrics.roc_curve(test_y,y_pred_gbtree,pos_label=1,sample_weight=None,drop_intermediate=True)
fpr_3, tpr_3, thresholds_3=metrics.roc_curve(test_y,y_pred,pos_label=1,sample_weight=None,drop_intermediate=True)
font = {'size': 18}
plt.plot([0,1],linestyle='dashed',color='darkgray',label='random chance')
plt.plot(fpr_1,tpr_1,color='b',label='gblinear')
plt.plot(fpr_2,tpr_2,color='g',label='gbtree')
plt.plot(fpr_3,tpr_3,color='r',label='gblinear+gbtree')

plt.legend(loc='lower right')
plt.title('ROC',font)
plt.xlabel('false positive rate',font)
plt.ylabel('true positive rate',font)
plt.axis([0, 1, 0, 1])
plt.show()

#输出特征重要性
import pandas as pd
importance_gbtree = bst_gbtree.get_fscore()
temp1_gbtree = []
temp2_gbtree = []
for key in importance_gbtree:
    temp1_gbtree.append(key)
    temp2_gbtree.append(importance_gbtree[key])
feature_importance = pd.DataFrame({
        'feature_id': temp1_gbtree,
        'importance_gbtree': temp2_gbtree,
    }).sort_values(by='importance_gbtree')
print(feature_importance)
# 导出特征重要性排序
feature_importance.to_csv('../Data/feature_importance.csv')
# 特征重要性可视化
from xgboost import plot_importance
from matplotlib import pyplot as plt
plot_importance(bst_gbtree,None,1)
plt.show()

# 预测16年样本流失概率
dtest16 = xgb.DMatrix('../Data/Alldata2016.txt')
y_pred_gblinear16=bst_gblinear.predict(dtest16)
y_pred_gbtree16=bst_gbtree.predict(dtest16)
y_pred = 0.3*y_pred_gblinear16+0.7*y_pred_gbtree16
results = pd.DataFrame(data=y_pred)
print(results)
results.to_csv('../Data/results2016.csv')