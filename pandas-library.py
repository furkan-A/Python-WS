import pandas as pd

    # SERIES
numbers = [1,2,3,4,5]
letters = ['a','b','c']
objects = ['x','y',7]

# pandas_series = pd.Series()
# pandas_series = pd.Series(numbers)
# pandas_series = pd.Series(letters)
# pandas_series = pd.Series(objects)

# print(pandas_series + "\n\n")

    # DATAFRAMES

s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])

# data = dict(apples = s1,  oranges = s2)
liste = [['Ahmet', 50], ["ALi", 80]]


df = pd.DataFrame(liste, columns = ['Name', 'Grade'])

print(df)

        # FILES


df = pd.read_csv('Players.csv')
# df = pd.read_json('doc.json', encoding="UTF-8")
# df = pd.read_excel('sample.xlsx')


print(df)




