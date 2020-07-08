n = 11
count = 0
flag = 0
while flag == 0:
    n += 1
    for itr in range(2, n):  # 1 to 12
        if n % itr == 0:  # 12%itr
            count = 1
    if count == 0:
        print(n)
        flag = 1
    if count == 1:
        count = 0
        continue

