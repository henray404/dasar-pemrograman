grade = input(" enter desired grade ")  # masukkan nilai yang diinginkan
# masukkan minimal nilai
minimum_avg = float(input(" enter minimum average required "))
# masukkan nilai yang sekarang
current_avg = float(input(" enter current average in course "))

# masukkan persentase nilai akhir
percentage_final = float(
    input(" enter how much the final counts as a percentage of the course grade "))

# hitung nilai akhir yang dibutuhkan
calculate = round((minimum_avg - (current_avg *
                  (100 - percentage_final) / 100)) * 100 / percentage_final, 2)


print(f"you need a score of {calculate} on the final to get {grade}")
