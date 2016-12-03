# Homework-session-3
prices = {
    "banana":4,
    "apple": 2,
    "orange":1.5,
    "pear":  3,
    }
stock = {
    "banana":6,
    "apple": 0,
    "orange": 32,
    "pear" : 15
    }
name = ["banana","apple","orange","pear"]
name.sort()
for key,value in prices.items():
    print(key)
    print("price : {0}".format(value))
total = 0
for key,value in prices.items():
    total += prices[key]*stock[key]
print(total)
    
    
