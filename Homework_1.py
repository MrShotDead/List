import random#virus.exe
a = []
b = []
c = []
for i in range(30):
    f = random.randint(1,100)
    if f<=30:
        a.append(f)
    elif f<=69 and f>=31:
        b.append(f)
    else:
        c.append(f)
print(a)
print(b)
print(c)