import pandas as pd

df = pd.read_csv("imdb.csv")

result = df.head(15)

result = df[["title","ranking"]].head(10)

# buradan imdb dosyasindan df ile istenilen filtreleme yapilabilir!

print(result)

























