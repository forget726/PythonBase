import pandas as pd
import os


path = './'
files = os.listdir(path)

for file in files:
    filenamandextention = file.split('F:\7.30\1-mcp')
    filename = filenamandextention[0] #文件名
    fileextention = filenamandextention[.xls]   #文件拓展名
    if fileextention not in 'xls':  #如果文件拓展名不是xls的话 就跳过
        continue
    
    df = pd.read_csv(file, sep = '\t', header = None)

    res = df["A"].str.split(',', expand=True)

    df['result'] = (df[0] * df[0] + df[1] * df[1]) ** 0.5 /df[2]
    
    df.to_excel(f"{filename}.xlsx", index = False)