# masukkan keceoatan dari pesawat jet
velocity = float(input("input jet velocity"))

# merubah nilai kecepatan dari km/jam menjadi m/s
v = round(velocity * 1000 / 3600, 2)
# jarak dari landasan sampai ke kecepatan yang diinginkan
s = float(input("input the distance from rest to take off"))

# kalkulasi percepatan
a = round((v ** 2) / (2 * s), 2)
# kalkulasi waktu dari kecepatan nol sampai kecepetan yang diinginkan
t = round(v / a, 2)

print(a)
print(t)
print(v)
