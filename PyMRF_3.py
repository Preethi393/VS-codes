nums = range(1,11)
even = lambda n: n % 2 == 0
print(even(4))

filterobj = filter(even, nums)
print("Result using filter-num: ",list(filterobj))

mapobj = map(even, nums)
print("Result using map-num: ",list(mapobj)) 