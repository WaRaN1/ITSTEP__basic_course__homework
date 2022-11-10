time1 = int(input("Яка зараз година?\n"))
time1_2 = time1 % 24
if time1_2 > 6 and time1_2 < 21:           #6 < time1_2 < 21:
    print("Друже, день навколо")
else:
    print("Друже, ніч на дворі")