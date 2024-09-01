# masukkan keceoatan dari pesawat jet
velocity = float(input("input jet velocity "))

# merubah nilai kecepatan dari km/jam menjadi m/s
velo = round(velocity * 1000 / 3600, 2)
# jarak dari landasan sampai ke kecepatan yang diinginkan
distance = float(input("input the distance from rest to take off "))

# kalkulasi percepatan
acceleration = round((velo ** 2) / (2 * distance), 2)
# kalkulasi waktu dari kecepatan nol sampai kecepetan yang diinginkan
time = round(velo / acceleration, 2)

print(F"the acceleration of the jet is {acceleration} m/s^2")
print(f"the amount of time from rest to takeoff {time} s ")
