
flow = float(input("enter flow rate"))   # m^3/s
height = float(input("enter height"))  # meter

efficient = float(0.90)  # persentase tenaga listrik yang didapatkan dari usaha
gravity = float(9.80)  # m/sec^2
water_mass = flow * 1000  # flow dikali oleh massa air tiap meter kubik (kg)

works = water_mass * gravity * height  # nilai usaha


megawatt = (works * efficient) / 10 ** 6  # mendapatkan nilai megawatt


print(megawatt)
