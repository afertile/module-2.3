my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while True:
    a = my_list[i]
    if a == 0:
        i += 1
        continue
    if a < 0:
        break
    print(a)
    i += 1