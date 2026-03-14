money = int(input())
count_500 = money // 500
money = money % 500
count_100 = money // 100
money = money % 100
count_50 = money // 50
money = money % 50
count_10 = money // 10
money = money % 10
print(count_500, count_100, count_50, count_10)