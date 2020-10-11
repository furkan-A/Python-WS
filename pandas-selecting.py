import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3), index = ['A','B','C'], columns = ['Column1','Column2','Column3'])


result = df
result = df['Column1']
result = type(df['Column1'])

# loc["row","column"] => loc["row"] => loc[":","column"]

result = df.loc["A"]
result = type(df.loc["A"])
result = df.loc[:,"Column1"]
result = df.iloc[2]         # indexi sayi ile secmek
result = df.loc[:,["Column1","Column2"]]
result = df.loc[:,"Column1":"Column2"]
result = df.loc[:,:"Column2"]
result = df.loc["A":"B",:"Column2"]
result = df.loc["C","Column3"]

# yeni column eklemek

df["Column4"] = pd.Series(randn(3), ['A','B','C'])
df["Column5"] = df["Column1"] + df["Column3"]

# result = df.drop("Column5", axis = 1, inplace = False)

result = df > 0
# print(result)

result = df[df > 0]         # filtreme in dataframe, columnlar da secilebilir
                            # NaN = Not a Number
result = df[(df["Column1"] > 1) & (df["Column2"] < 0) ]

# print(df)
print(result)









