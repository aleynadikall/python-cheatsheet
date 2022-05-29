i = 0

while i < 10:
    if i == 5:
        break
    print("i:", i)
    i += 1

j = 0

while j < 10:
    if j == 3 or j == 5:
        j += 1
        continue
    print("j:", j)
    j += 1
