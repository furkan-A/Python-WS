
class Circle:
    pi = 3.14

    def __init__(self, yaricap = 1):  # eger bir deger atanmazsa 1 olarak kabul edilecek 
        self.yaricap = yaricap
        
    def cevre_hesapla(self):
        return 2 * self.pi * self.yaricap

    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)
    


c1 = Circle(4)

print(type(c1))
print(f'c1\'in Alanı: {c1.alan_hesapla()} Çevresi = {c1.cevre_hesapla()}')




