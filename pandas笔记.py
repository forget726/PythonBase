import pandas as pd

# df = pd.read_csv('nba.csv')

# 设置最大列数，禁止用……表示
pd.set_option('display.max_columns', None)
# 禁止列表分开（如果不设置列太多会分两次显示）
pd.set_option('display.expand_frame_repr', False)
# 设置最大行数，禁止用……表示
pd.set_option('display.max_rows', None)
# print(df.to_string())
# print(df)
# print(df.head(50))
# print(df.tail(50)
# js = pd.read_json('sites.json').to_string()
# print(js)
# 字典格式的 JSON
s = {
    "col1":{"row1":1,"row2":2,"row3":3},
    "col2":{"row1":"x","row2":"y","row3":"z"}
}

# 读取 JSON 转为 DataFrame
df2 = pd.DataFrame(s)
url = "https://static.runoob.com/download/sites.json"
df3 = pd.read_json(url)
print(df2)
print(df3)

