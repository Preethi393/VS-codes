from functools import reduce

num = range(1,6)
myfunc = lambda x, y : x * y

print("Nums: ", num)
result = reduce(myfunc, num)
print(result)

