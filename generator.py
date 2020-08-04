
def cube():
    for i in range(5):
        yield i ** 3        # yield : her dongude gerceklestirilen degeri tutmazve siler 
                            # sadece en son degeri tutan keyword
                            # o yuzden --> cok buyuk dongulerde hafizada yer kaplamamak icin kullanilir

generator = cube()

print(generator)            # output : <generator object cube at 0x03719568>


iterator = iter(generator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
# print(next(iterator))     # bir sonraki deger olmadigi icin hata dondurur.


liste = [j**3 for j in range(5)]
print(liste)

print("-----------------------")

liste2 = (k**3 for k in range(5))  # generator liste
print(liste2)

print(next(liste2), "\n")


