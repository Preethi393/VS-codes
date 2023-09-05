'''
print("Let's practice everything.")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")
print("--------------")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
print(secret_formula(50))

start_point = 10000
beans, jars, crates = secret_formula(start_point)
print(secret_formula(10000))

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.") 
start_point = start_point / 10
print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string

print("We'd have {} beans, {} jars, and {}crates.".format(*formula)) 


stuff = "Helloo this is my practice session"
def break_words(stuff):
    words = stuff.split(' ')
    return words
print(break_words(stuff)) 


def sorted_words(word):
    return sorted(word)
word = ('hello')
print(sorted_words(word)) 

def print_first_word(words):
    word = words.pop(1)
    print(word)
words = ['happy' , 'sad', 'excited', 'thrilled']
print_first_word(words)
print(words) 

def print_last_word(words):
    word = words.pop(-1)
    print(word)
words = ['happy' , 'sad', 'excited', 'thrilled']
print_last_word(words)
print(words) 


def sort_sentence(sentence):
    words = break_words(sentence)
    return sorted_words(words)
print(sort_sentence(sentence = 'Hi, are you doing good')) 

def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
print(print_first_and_last(sentence= "whats up")) 

the_count = [1, 2, 3, 4, 5]
fruits =['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print(f'This is count {number}')

for fruit in fruits:
    print(f'A fruit of type {fruit}')

for i in change:
    print('I got {}'.format (i))

elements = []
for i in range(0,6):
    print(f"Adding {i} to the list")
    elements.append(i)

for i in elements:
    print(f"Elements was: {i}") 

states = {
'Oregon': 'OR',
'Florida': 'FL',
'California': 'CA',
'New York': 'NY',
'Michigan': 'MI'
}    

cities = {
'CA': 'San Francisco',
'MI': 'Detroit',
'FL': 'Jacksonville'
}
cities['NY'] = 'New York'
cities['OR'] = 'PorLand'
print(cities['CA']) 



__a = 10
print(__a)

__str__ = 1
print(__str__)

_ = 20
print(_) 

from math import fabs


print(fabs(-25)) # returns absolute float value i.e 25.0
print(abs(-25)) # returns absolute value i.e 25    '''  
