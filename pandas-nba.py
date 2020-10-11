import pandas as pd

df = pd.read_csv("Players.csv")

# Toplam kaç kayit var?
result = len(df.index)

# Ilk 10 kayit 
result = df.head(10)

# Tum oyuncularin kilo ortalamasi
result = df["weight"].mean()

# En uzun boy?
result = df["height"].max()

# En uzun boylu Oyuncu kimdir?
result = df[df["height"] == df["height"].max()]["Player"].iloc[0]

# 1990-1995 yillari arasinda dogan oyuncularin isimleri ve takimlari 
result = df[(df["born"] >= 1990) & (df["born"] < 1991)][["Player","collage"]].sort_values("Player", ascending = True)

# "Jimmy Darden" isimli oyuncunun oynadigi takim 
result = df[(df["Player"] == "Jimmy Darden")]["collage"]

# Kaç farkli college mevcut
result = len(df.groupby("collage"))
result = df["collage"].nunique()

# College'lara gore oyuncuların ortalama kilo bilgisi
result = df.groupby("collage").mean()["weight"]

# her collage'den kac oyuncu gelmistir
result = df["collage"].value_counts()

# Oyuncular icerisinde "and" gecen kayitlari bul
# df = df.dropna()                # NaN olan degerleri siliyoruz
df.dropna(inplace = True)
result = df[df["Player"].str.contains("and")]


print(result)
