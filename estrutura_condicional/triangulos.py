r1 = float(input("Primeiro segmento: "))
r2 = float(input("Primeiro segmento: "))
r3 = float(input("Primeiro segmento: "))

if r1 == r3 and r1 == r2:
    print("Equilátero")
elif r1 == r2 or r3 == r1 or r3 == r2:
    print("isosceles")
else:
    print("escaleno")
