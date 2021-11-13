money = 1000
if money > 500:
    money -= 500
print(money)

if money > 500:
    money -= 500
else:
    money += 500
print(money)

if money > 500 \
        and money < 1000:
    money -= 500
elif money >= 1000:
    money += 1500
else:
    money += 500
print(money)

money = 1000
if money > 500:
    if money < 2000:
        print('<=2000', money)
    else:
        print('>=2000', money)

