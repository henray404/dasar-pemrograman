x1 = float(input("input x1 value "))  # masukkan nilai x1
x2 = float(input("input x2 value "))  # masukkan nilai x2
y1 = float(input("input y1 value "))  # masukkan nilai y1
y2 = float(input("input y2 value "))  # masukkan nilai y2

m = (y2 - y1) / (x2 - x1)  # menghitung kemiringan / slope

xmid = (x1 + x2) / 2  # menghitung titik tengah dari sumbu x
ymid = (y1 + y2) / 2  # menghitung titik tengah dari sumbu y

# menghitung kemiringan dari sumbu tegak lurus dari segmen garis asli
mperpendicular = -1/m


# mwnghitung titik di mana sebuah garis memotong sumbu y
b = ymid - mperpendicular * xmid

print(m)
print(xmid)
print(ymid)
print(mperpendicular)
print(b)

print(f"origin 2 points ({x1}, {y1}), ({x2}, {y2})")
print(f"y = {mperpendicular}x + {b}")
