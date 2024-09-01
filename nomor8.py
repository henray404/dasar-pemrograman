person = int(input("input total person per day "))

new_toilet = 2  # liter per flush
person_toilet = 3  # person per toilet
old_toilet = 15  # liter per flush
avg_flush = 14  # flush per day
cost_intall = 150  # dollar per install


toilet = int(person / person_toilet)  # count how many toilet
toilet_cost = toilet * cost_intall
magnitude = (toilet * avg_flush * old_toilet) - (toilet *
                                                 avg_flush * new_toilet)  # calculate the magnitude

print(f"the cost for intalling new toilet is {toilet_cost}")
print(f"the estimate fot the magnitude is {magnitude} liter/day ")
