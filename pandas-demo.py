
import pandas as pd

df = pd.read_csv("datasets/pandas-taobao/taobao_data.csv")

# 查看表的数据信息
print(df.info())

# 查看表的描述性信息
print(df.describe())

# region 数据选择

# 行的选取
rows = df[0:3]
print(rows)

# 列的选取
cols = df[['宝贝', '价格']]
print(cols.head(5))

# 块的选取

region = df.loc[0:3, ['宝贝', '价格']]
print(region)

# 创建新列
df['销售额'] = df['价格']*df['成交量']
print(df.head())

# 过滤行

filter_rows = df[(df['价格'] < 100) & (df['成交量'] > 1000)]
print(filter_rows)

# endregion

# region 数据整理，排序，分组，分割，合并，变形

# 排序
dfi = df.set_index("位置")
dfi = dfi.sort_index()
print(dfi.head())

df2 = df.set_index(["位置", "卖家"]).sort_index(0)
print(df2.head())

# 分组
df_mean = df.drop(["宝贝", "卖家"], axis=1).groupby("位置").mean().sort_values("成交量", ascending=False)
print(df_mean)

df_sum = df.drop(["宝贝", "卖家"], axis=1).groupby("位置").sum().sort_values("成交量", ascending=False)
print(df_sum)

# 分割
dfd = df[30:40][["位置", "卖家"]]
print(dfd)

# endregion


