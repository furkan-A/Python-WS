import numpy as np

# result = np.array([1,3,5,7,9])
# result = np.arange(1,10)
# result = np.arange(0,100,5)        # artis yaparak olusan dizi
# result = np.ones(10)
# result = np.zeros(10)              # 0'lardan olusan dizi
# result = np.linspace(0,100,5)      # sayi araligini esit parcaya boler
# result = np.random.randint(0,10)   # random sayi uretir
# result = np.random.randint(1,20,3) # 1 le 20 arasindan 3 sayi donderir
# result = np.random.rand(5)         # 0 la 1 aarsından 5 sayi uretir
# result = np.random.randn(5)        # eksileri de dahil eder
np_array = np.arange(50)
result = np_array.reshape(5,10)

result2 = result
print(result.sum(axis = 1))         # satir toplamlari
print(result.sum(axis = 0))         # sutun toplamlari

rnd_numbers = np.random.randint(1,100,10)
print(rnd_numbers)

# result = rnd_numbers.max()
# result = rnd_numbers.min()
# result = rnd_numbers.mean()
# result = rnd_numbers.argmax()
result = rnd_numbers.argmin()       # min sayinin indeksi

result = rnd_numbers[::-1]          # diziyi tersten yazdirma
result = rnd_numbers >= 50          # her elemani 50 ile karsilastirir

# result = np.vstack(parametre1, parametre2) # yatayda dizi birlestirir

print(result)
