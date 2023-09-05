num = input("Enter any sequence of numbers: ")
# lstnums = num.split(',')

# res = 0
# for i in lstnums:
#     res += int(i)
# print(res)

lstnums = list(map(int, num.split(",")))
print(sum(lstnums))