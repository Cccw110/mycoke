import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
import pickle

# 设置输出格式，确保中文对齐
pd.set_option('display.unicode.east_asian_width', True)

# 读取数据集（请确保文件路径正确）
insurance_df = pd.read_csv('C:/Users/Lenovo/insurance-chinese.csv', encoding='gbk')

# 提取特征与目标变量
output = insurance_df['医疗费用']
features = insurance_df[['年龄', '性别', 'BMI', '子女数量', '是否吸烟', '区域']]

# 数据预处理：独热编码分类变量
features = pd.get_dummies(features)

# 划分训练集与测试集（80:20）
x_train, x_test, y_train, y_test = train_test_split(
    features, output, train_size=0.8, random_state=42
)

# 模型训练：随机森林回归
rfr = RandomForestRegressor(n_estimators=100, random_state=42)
rfr.fit(x_train, y_train)

# 模型评估
y_pred = rfr.predict(x_test)
r2 = r2_score(y_test, y_pred)
print(f'模型评估：R² 分数 = {r2:.4f}')

# 保存模型为 pickle 文件
with open('rfr_model.pkl', 'wb') as f:
    pickle.dump(rfr, f)
print('模型已成功保存为 rfr_model.pkl')