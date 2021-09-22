#задание 1
time = int(input("Введите количество секунд: "))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("дн:час:мин:сек-> %d:%d:%d:%d" % (day, hour, minutes, seconds))
# 2
num_list = []
for num in range(1, 1001):
    if num % 2 != 0:
        num_list.append(num ** 3)
sum_seven = 0
for num in num_list:
    tmp = num
    sum_num = 0
    while num != 0:
        sum_num += num % 10
        num //= 10
    if sum_num % 7 == 0:
        sum_seven += tmp
print(sum_seven)
for i in range(0, (len(num_list))):
    num_list[i] += 17
    sum_seven = 0
    for num in num_list:
        tmp = num
        sum_num = 0
        while num != 0:
            sum_num += num % 10
            num //= 10
        if sum_num % 7 == 0:
            sum_seven += tmp
print(sum_seven)
#задание 3
for i in range(1, 101):
    if i % 10 == 1 and i != 11:
        print(str(i) + ' процент')
    elif i % 10 in [2, 3, 4] and i not in [12, 13, 14]:
        print(str(i) + ' процента')
    else:
        print(str(i) + ' процентов')