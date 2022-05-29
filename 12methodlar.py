liste = [1, 2, 3, 4, 5, 6]
a = "araba"

print(len(a))  # 5
print(len(liste))  # 6

print(a.startswith("a")) #a stringi a ile basliyor mu sorusuna true ya da false degerini dondurur.

print(a.startswith("ar"))
print(a.endswith("a"))
print(a.endswith("s"))

a = a.replace("a","o")
print(a)

liste.append("Python") # liste sonuna Python eklenir.
print(liste)

liste.pop() # son elemani (indeks vermezsek) cikarir.
print(liste)

liste.pop(1) #2.elemani siler.
print(liste)