nums = range(1,11)
print(list(nums))

sq = lambda n : n*n

#Approach 1

# sqs = []
# for i in nums:
#     sqs.append(sq(i))
# print(sqs)

# # Approach 2
# sqs = [sq(i) for i in nums]
# print(sqs)

# # Approach 3
# sqs = [i * i for i in nums]
# print(sqs)

# Approach 4 
# mobject = map(sq, nums)
# # print("List of square of nums: ", list(mobject))
# print("Tuple of square of nums: ", tuple(mobject))


from math import factorial
print("List of factorial of nums using map: ", list(map(factorial, nums)))