banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
dictMoney = {}

for b in banknotes_coins:
    b = str(b)
    dictMoney.update({b : 0})

# print(dictMoney)

dictMoney["100"] = 1
dictMoney["20"] = 1
dictMoney["5"] = 1
dictMoney["0.5"] = 1
dictMoney["50"] = 1
dictMoney["20"] = 3
dictMoney["5"] = 2
dictMoney["2"] = 2
dictMoney["100"] = 2
dictMoney["50"] = 2
dictMoney["2"] = 3

# print(dictMoney.get("100"))
# print(dictMoney)


for b in dictMoney.keys():
    print("nominał: ", b, "ilość: ", dictMoney.get(b))