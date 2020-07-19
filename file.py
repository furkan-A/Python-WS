name = "Furkan"
surname = "AKTAŞ"
age = 21
metin = "hello there how are you"

print(f"My name's {name} {surname} and I'm {age} years old.")


name = name.strip()  # basindaki white char lari atiyor
metin = metin.split(' ') # verilen parametreye gore metni parcalar.
print(metin)

metin2 = '*'.join(metin)
print(metin2)


# dictionary =>  plakalar = { 'key' : 'value', , , }
# tuple'larin atandiktan sonra elemanlari degistirilemez

users = { 
    "furkan" : {
        "age" : 21,
        "mail" : 'furki@gmail.com',
        "roles" : ["admin", "user"]
    },
    "fulya" : {
        "age" : 10,
        "mail" : 'fulya@gmail.com',
        "roles" : ["user"]
    }
}

print(users['furkan']['age'])

