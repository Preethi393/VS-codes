'''
operation =int(input("Enter operations(1-4): "))
x = int(input("Enter first number "))
y = int(input("Enter second number "))
if operation == 1:
    print(x + y)
elif operation == 2:
    print(x - y)
elif operation == 3:
    print(x * y) 
elif operation == 4:
    print(x / y) 
else:
    print("No such operation")  

# Program make a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
    else:
        print("Invalid Input")



tupl_dishes = ('Pulao', 'Shahi Paneer', 'Palak Paneer', 'Gobi Manchurian')
my_plate = []
for itr in tupl_dishes:
  if itr == 'Shahi Paneer' or itr == 'Palak Paneer':
        my_plate.append(itr)
  else:
    pass 
print(my_plate)

tupl_dishes = ('Pulao', 'Shahi Paneer', 'Palak Paneer', 'Gobi Manchurian')
my_plate = []
for itr in tupl_dishes:
  if itr == 'Shahi Paneer' or itr == 'Palak Paneer':
    my_plate.append(itr)
  elif itr == 'Pulao':
    my_plate.append(itr +' Salt')
  else:
    pass

print(my_plate) 


tupl_dishes = ('Pulao', 'Shahi Paneer', 'Palak Paneer', 'Gobi Manchurian')
for itr in range(len(tupl_dishes)):
    print(itr, tupl_dishes[itr])

# or

for itr in range(4):
    print(itr, tupl_dishes[itr])

itr = 0
while True:
    print(itr)
    itr = itr + 1
    if itr > 100:
        break
    else:
        pass
    

for i in range(20):
    if i % 2 != 0:
        continue
    else:
        print(i)



for i in range(20):
    if i % 2 != 0:
      continue
    else:
        print("Hi, number is {}".format(i))


lst = [1,2,3,1,1,2,3,2]
N = 2
def delete_nth(lst, N):
    new_lst =[]
    for itr in lst:
        #print(itr)
        if (new_lst.count(itr)< N ):
            new_lst.append(itr)
        else:
            pass
    return new_lst 
print(delete_nth(lst, N))


fruits = {'Apple': 'Red', 'Mango': 'Yellow'}
for k,v in fruits.items():
    print(k,v) 

names = ['Jim', 'Jack','Tom']
age = [10,20,30]
names_age = zip(names,age)
names_age_lst = list(zip(names,age))
print(names_age_lst)
names_age_tupl = tuple(zip(names,age))
print(names_age_tupl)
names_age_dict = dict(zip(names,age))

print(names_age_dict)

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
print(A0)

for k,v in names_age:
    print(k,v) 

#Iterator

lst = [1,2,3,4,5]
itr = iter(lst)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))


itr = iter(list(range(10)))
print(next(itr))
print(next(itr)) 

lst_frt = ['Apple','Banana','Orange', 'Cherry', 'Grapes']
itr = iter(lst_frt)
def itr_fruits(lst_frt):
    for itr in lst_frt:
        print(itr)
print(next(itr))  
print(next(itr))  
print(next(itr))  
print(next(itr))  
print(next(itr))  
print(next(itr))  

#Generator

lst_nums = [5,20,44,55]
def gen_sq_nums(lst_nums):
    for itr in lst_nums:
        yield(itr*itr)
ret_num = gen_sq_nums(lst_nums)
print(ret_num)
 
print(next(ret_num))
print(next(ret_num))
print(next(ret_num))
print(next(ret_num)) 

# List Comprehension

lst = [55,50,49]
lst_sqrs = []
for itr in lst:
    lst_sqrs.append(itr**2)
print(lst_sqrs)

lst_sqrs = [itr**2 for itr in lst]
print(lst_sqrs) 

a = 3
b = 6
def div(a,b):
    if a < b :
        a,b = b,a  #swap a and b only if a is less than b
    print(a/b)
div(a,b) 

name = 'Preethi'
age = 29
print(f"Hello, {name}. you are {age} years old") 

print(f'{2 * 3}')

def to_lowercase(input):
       return input.lower()

name = "Eric Idle"
print(f"{to_lowercase(name)} is funny.") 

x = ('apple', 'banana', 'cherry')
y = enumerate(x)

print(list(y))  

lst = (55,50,49)
x = enumerate(lst)
print(dict(x)) 

alphabet_str =  "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z"
d1 = dict((value,key) for key, value in enumerate(alphabet_str.split(','), start= 1))
print(d1)

name = 'jashith'
def name_upper(name):
    return name.upper()

n = name_upper(name)
print(n) 

def hello_world():
    print('Hello world')
    print('My life is crazy')
hello_world()

def GuessTheCountry(cur):
    if cur == 'GBP':
        print('Country is UK')
    elif cur == 'USD':
        print('Country is US')
    elif cur == 'INR':
        print('Country is India')
    else:
        print("No such currency")
print("Enter The Currency ") 
cur = input('>')
GuessTheCountry(cur)      

def area_of_circle(r, pi=3.14):
    print(pi * r * r)
area_of_circle(10)

def print_stud_det(student_name, *student_marks):
      print(type(student_name))

      for itr in student_marks:
        print("Student marks is {}". format(itr))

print_stud_det("ABC",90,100,80) 

def print_person_det(**person_detls):
      print(type(person_detls))

      for per,sal in person_detls.items():
        print("Name is {}, Salary is {} ". format(per,sal))

print_person_det(Preethi = 15000, ABC = 16000)

sum = lambda arg1, arg2 : arg1 + arg2
print("value of total:",sum(10,20))
print("value of total:",sum(20,20)) 


area = lambda pi, radius : pi * radius * radius
print("The area of circle is: ", area(3.14,5))

a = 99 # Global Variable
def func():
    a = 88 # Local variable
    print(a)
func()  
print(a)
   

def print_person_det(**person_detls):
      print(type(person_detls))
     
      for per,sal in person_detls.items():
        print("Name is {}, Salary is {} ". format(per,sal))

print_person_det(Preethi = 15000, ABC = 16000) 

vowel = 'a', 'e', 'i', 'o', 'u'
char = input('>> ')
filt = lambda char : 'Vowel' if char in vowel else 'Consonant'
print(filt(char))

def print_pattern(n):
    for itr in range(1, n+1):
        print(str(itr)*itr)

print_pattern(3)

# or

def prt_pat(n):
    for itr in range(1, n+1):
        for itr1 in range(itr):
            print(itr, end = " ")    
        print('\n')
prt_pat(3)

def parent():
    print("This is a call from the parent function")
def first_child():
    print("Printing from first_child function")
def second_child():
    print("Printing from second_child function")
first_child()
second_child()


def uppercase(func):
    def wrapper_func():
        return func().upper()
    return wrapper_func    

@uppercase
def greet():
    return "Hello dear friends"

greet = uppercase(greet)
greet
greet()     

def calc_sqrs(n):
    return n * n 
numbers = (1,2,3,4)
result = map(calc_sqrs , numbers)
print(result)
numsqr = list(result)
print(numsqr)

   # or

numbers = (1,2,3,4)
result = map(lambda x : x*x, numbers)
numsqr = list(result)
print(numsqr)

def CubeNum(n):
    return n**3
num = (3,4,5,6)
result = map(CubeNum , num)
print(result)
cube = list(result)
print(cube)

num1 = [4,5,6]
num2 = [5,6,7]
result = map(lambda n1, n2 : n1+n2, num1, num2)
print(result)
print(list(result))

alphabet = ['a','b','c','d','e','f','i','o','u','p']
def FilterVowels(alphabet):
    vowels = ['a','e','i','o','u']
    if alphabet in vowels:
        return True
    else:
        return False 
filteredVowels = filter(FilterVowels,alphabet)
for vowels in filteredVowels:
    print(vowels) 

from functools import reduce


nums = (1,2,3,4,5,6)
sum = reduce(lambda a,b: a+b,nums)
print(sum) 

def add(a,b):
    return a + b
nums = [1,2,3,4,5,6]
result = reduce(add, nums)
print(result)  

import copy

lst1 = [[1,10],2,'abc']
lst2 = copy.copy(lst1)
#print(lst1)
#print(lst2)

lst2.append("Hello")
print(lst2)
print(lst1)

lst1[0][1] = 2.561
print(lst1)

print(lst2)

lst2[1] = 3
print(lst2)
print(lst1)


print(__name__)
import math
print(math.ceil(10.1))
print(math.__name__)

try:
    n1 = int(input('> '))
    n2 = int(input('>> '))
    n3 = print(n1/n2)
except:
    print("You cant divide a number by zero")
    try:
         n1 = int(input('* '))
         n2 = int(input('-> '))
         n3 = print(n1/n2)
    except:
        print("Again you are trying division by Zero")


try:
    n1 = int(input('> '))
    n2 = int(input('>> '))
    n3 = print(n1/n2)
    fp = open(r'Hello_there.txt', 'r')
except ZeroDivisionError:
    print("You cant divide a number by zero")
    try:
         n1 = int(input('* '))
         n2 = int(input('-> '))
         print(n1/n2)
    except ZeroDivisionError:
        print("Again you are trying division by Zero")
except FileNotFoundError:
    print("Oops, the file doesnt exist, please check its path") 
except:
    print("please debug properly")    
else:
    print("Good, no errors")
finally:
    print("Ok, Bye")  

try:
    sal = float(input('> '))
    assert sal >=10000
    print(sal)
except AssertionError:
    print("Please enter your salary properly") 

sal = float(input('> '))
assert sal >=100
print(sal) 

def ageEvenOrOdd(age):
    if age < 0:
        raise ValueError("Oops, Age cant be less than zero ")
    elif age == 0:
        print("New Born Baby")
    elif age % 2 == 0:
        print("Age is Even")
    else:
        print("Age is Odd") 
ageEvenOrOdd(-1) 

# program to print the reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal) 

import math
try:
    num = int(input("Enter Number: "))
    number = math.ceil(num)
except(SyntaxError,TypeError,ValueError)as e:
    print("Name Error: Here's the error : \n",e) '''


