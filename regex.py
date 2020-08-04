import re

str = "Python Programlama dili Ogrenme Uygulamasi"

result = re.findall("[abc]", str)       # [abc]
result = re.findall("[a-f]", str)       # [abcdef]
result = re.findall("[0-7]", str)       # [01234567]
result = re.findall("[1-47]", str)      # [12347]
result = re.findall("[^abc]", str)      # abc disindaki karekterler
result = re.findall("[^0-9]", str)      # rakam disindaki karektereler
result = re.findall("[abc]", str)
result = re.findall("[abc]", str)
result = re.findall("[abc]", str)


print(result)


"""   diger RegEx metodları ve kullanimlari

https://www.w3schools.com/python/python_regex.asp

"""