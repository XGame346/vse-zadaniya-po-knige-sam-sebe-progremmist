import cubed
x=int(input("Введите x "))
print(cubed.cubed(x))
bratok=[]
with open ("p1.txt", "r") as f:
    bratok.append(f.read())
print(bratok)
