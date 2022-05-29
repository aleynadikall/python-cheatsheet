a = "Python"
b = [1,2,3,4,5,6,7]

print(a[0])
print(a[2])

print(len(a))
print(len(b))

print(a[len(a)-1]) #a'nin son elemanini bulmak icin
print(b[len(b)-1]) #b'nin son elemanini bulmak icin

print(a[0:2]) #Py
print(a[2:]) #thon
print(a[:4]) #Pyth
print(b[2:]) #[3,4,5,6,7]
print(b[0:6:2]) #[1,3,5]
print(b[::2]) #[1,3,5,7]

#SOZLUK
a = {"Elma":3,"Armut":4,"Kiraz":5}
print(a["Elma"]) #3
print(a["Armut"]) #4
#print(a["Çilek"]) yazmak hatalidir. (KeyError)

