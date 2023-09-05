'''
class Shark:
    def swim(self):
        print("The shark is swimming \n")
    def be_awesome(self):
        print("The Shark is being awesome \n")
sammy = Shark()
vicky = Shark()

print(type(sammy))

sammy.swim()
sammy.be_awesome()
vicky.swim()
vicky.be_awesome() 

class B(object):
    def first(self):
        print("First Method")
    def second(self):
        print("Second Method")
python = B()
B.first(python) 
B.second(python)   

class B(object):
    def first(self):
        print("First Method")
    def second(self):
        print("Second Method")
python = B()
python.first()
python.second()


class Shark:
    def __init__(self, name):
        self.name = name
    def swim(self):
        print("The shark {} is swimming \n".format(self.name))
    def be_awesome(self):
        print("The shark {} is being awesome \n".format(self.name))
sammy = Shark('Jai')
print(sammy.name)
sammy.swim()
sammy.be_awesome()

class Shark(object):
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def swim(self):
        print("The %s shark %s is swimming \n"%(self.color,self.name))
    def be_awesome(self):
        print("The %s shark %s is being awesome \n"%(self.color,self.name,))
sammy = Shark('Veeru','White')
vicky = Shark('Jai', 'Blue')
sammy.swim()
sammy.be_awesome()
vicky.swim()
vicky.be_awesome() 

print(getattr(sammy,'name'))
print(getattr(vicky,'name'))
print(hasattr(sammy, 'name'))
setattr(sammy, 'color','Black')
print(getattr(sammy,'color'))
delattr(sammy,'color')  


class Shark:
    #This is a class to create Shark
    location = 'Ocean' # Class variable
    animal_type = 'Fish' # Class variable

    def __init__(self, name = 'Blue Whale'):
        self.name = name # Instance / Object variable

    def swim(self):
        print("The shark %s is swimming \n"%(self.name))

    def be_awesome(self):
        print("The shark %s is being awesome \n"%(self.name))
sammy = Shark()
print(sammy.location)
print(sammy.name)
print(sammy.animal_type)

# Inheritance

class A:
    def __init__(self):
        print('In A init')

    def feature1(self):
        print('Feature 1 working')
    def feature2(self):
        print('Feature 2 working')
a1 = A()
a1.feature1()


class B(A):
    def __init__(self):
        super().__init__()
        print('In B init')

    def feature3(self):
        print('Feature 3 working')
    def feature4(self):
        print('Feature 4 working')   
a1 = B()  


class Fish:
    def __init__(self,first_name, last_name = 'Fish',skeleton = 'Bone', eyelids = False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
    def swim(self):
        print("This fish %s swimming."%(self.first_name))
    def swim_backwards(self):
        print("This fish %s can swim backwards."%(self.first_name))

class GoldFish(Fish):
    pass
cassey = GoldFish('Nemo','Fish')
cassey.swim_backwards() 
print(cassey.skeleton) 

class Shark(Fish):

     def __init__(self,first_name, last_name = 'Shark',skeleton = 'Cartilege', eyelids = True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
     def swim_backwards(self):
        print("This fish %s can't swim backwards, it sinks and swims back"%(self.first_name))

sammy = Shark('Jacky')
print(sammy.last_name)
print(sammy.skeleton)
sammy.swim_backwards()

class Trout(Fish):
    def __init__(self, first_name,water = 'River'):
        self.water = water
        super().__init__(first_name)
trout = Trout('Nemo')
print(trout.first_name)
print(trout.water)
print(trout.swim()) 

class Coral():
    def community(self):
        print("Coral lives in a community")
class Anemone:
    def print_clownfish(self):
        print("Anemones protect clownfish")
    def community(self):
        print("Anemones dont live in a community")
class Coral_reef(Anemone,Coral):
    pass
   
coral = Coral_reef()
coral.community()
coral.print_clownfish()
print(Coral_reef.__mro__)
print(issubclass(Coral_reef,Anemone)) 

class Mammal(object):
  def __init__(self, mammalName):
    print(mammalName, 'is a warm-blooded animal.')
  
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    super().__init__('Dog')

d1 = Dog() 

class Coral():
    def community(self):
        print("Coral lives in a community")

class Anemone():
    def __init__(self,name,private_location = 'borough'):
        self._name = name  #private
        self.__loc = private_location  #strongly private

    def __print_clownfish(self):
         print("Anemones protect clownfish")
         print("Its location is %s"%(self.__loc))

    def community(self):
        print("Anemones dont live in community")
        self.__print_clownfish()

class Coral_reef(Anemone,Coral):
    pass

coral = Coral_reef('Jacky')
coral.community()

coral._print_clownfish() 

# Example for Polymorphism 

def in_the_pacific(fish):
    fish.swim()
    fish.swim_backwards()
    print(fish.skeleton)
    
class Fish:
    def __init__(self,first_name, last_name = 'Fish',skeleton = 'Bone', eyelids = False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
    def swim(self):
        print("This fish %s swimming."%(self.first_name))
    def swim_backwards(self):
        print("This fish %s can swim backwards."%(self.first_name))

class Shark(Fish):
    def __init__(self,first_name, last_name = 'Shark',skeleton = 'Cartilege', eyelids = True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids
    def swim_backwards(self):
        print("This fish %s can't swim backwards, it sinks and swims back"%(self.first_name))

cassey = Fish('Cassey')
sammy = Fish('Sammy')
joey = Shark('Joey')

lst_objects = [cassey,sammy,joey]

for itr in lst_objects:
    in_the_pacific(itr) 

# Composition

class Rocket:
    def __init__(self, name, distance):
        self.name = name
        self.distance = distance
    def launch(self):
        return "%s has reached %s" %(self.name, self.distance)

class MarsRoverComp():
    def __init__(self,name, distance, maker):
        self.rocket = Rocket(name, distance)
        self.maker = maker
    def get_maker(self):
        return "%s launched by %s" %(self.rocket.name,self.maker)

mars_rov = MarsRoverComp("ISRO Mars Rover",'500000 kms','ISRO')
print(mars_rov.get_maker())  

class Error(Exception):
    pass
class ValueTooSmallError(Error):
    pass
class ValueTooLargeError(Error):
    pass

number = 10

while True:
    try:
        i_num = int(input("Enter a Number: "))
        if i_num < number:
            raise ValueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        else:
            print("Congratulations! You guessed it correctly")
        break
    except ValueTooSmallError:
        print("This value is too small, try again!")
        print()
    except ValueTooLargeError:
        print("This value is too large,try again!") 

class Book():
    def __init__(self,book_name,author,page):
        self.book_name = book_name
        self.author = author
        self.page = page
    def __str__(self):
        return "Title: {}, Author : {}, Pages : {} ".format(self.book_name,self.author,self.page)
    def __del__(self):
        print("A book is deleted")
bk = Book("Python", "Dip", 300)
print(bk.__str__())
print(bk)
del(bk)
bk.__del__()  '''

for letter in 'Python':
    print("Current letter :", letter)

