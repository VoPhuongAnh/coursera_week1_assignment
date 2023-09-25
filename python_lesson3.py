x = 10
x = x + 3
x += 3
# line 3 bang voi line 2, duoc goi la argumented assignment operator
y = x != 13
print(y)
z = x == 13
print(z)

price = 5
print('The result: ' + str(price > 10 or price < 40))

price = 5
print('The result: ' + str(price > 10 and price < 40))

price = 5
print('The result: ' + str( not price > 10 and price < 40))
# line 17 la revert ket qua line 14

temperature = 30
if temperature > 30 :
    print("It's a hot day.")
    print('Drink water!')
elif temperature > 20: # (20,30]
    print("It's a nice day.")
elif temperature > 10:
    print("It's a bit cold.")