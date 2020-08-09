import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos/1")

result = json.loads(result.text)

print(type(result))
print(result, "\n\n\n")

    #  Döviz Exchange Uygulaması


api_url = "https://api.exchangeratesapi.io/latest?base"

bozulan_doviz = input("Bozdurmak istenen doviz turu: ")
alinan_doviz = input("Alinacak bir doviz turu: ")

miktar = int(input(f"Ne kadar {bozulan_doviz} bozduracaksiniz: "))

sonuc = requests.get(api_url + bozulan_doviz)
sonuc = json.loads(sonuc.text)

print("1 {0} = {1} {2}".format(bozulan_doviz, sonuc["rates"][alinan_doviz], alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz,miktar * sonuc["rates"][alinan_doviz],alinan_doviz))

