# TEST 1:-------------------------------------------
# we create objects when we instantiate a class

class Test:
    test_var = 'string'

# instantiantion
instance = Test()
# print(instance.test_var)


# TEST 2:-------------------------------------------
class Grade:
    minimal_passing = 65

    def explanation(self):
        print('The minimal passing grade is {}.'.format(self.minimal_passing))

statement = Grade()
statement.explanation()

# TEST 3:-------------------------------------------
class DistanceConverter:
    kms_in_a_mile = 1.60934

    def convert_miles_to_kms(self, miles):
        return miles * self.kms_in_a_mile

converter = DistanceConverter()
kms_10 = converter.convert_miles_to_kms(10)
print(kms_10)   


# TEST 4:------------------------------------------- 
# Constructors
class Shouter:
    def __init__(self, phrase):
        if type(phrase) == str:
            print(phrase.upper())

shout1 = Shouter("Hello World!!")
shout2 = Shouter("Hello back!")


# TEST 5: Circle Diameter (Constructors)
class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print(f"New circle with diameter: {diameter}")

teaching_table = Circle(36)

# TEST 6: Instance Variables
# create class
class FakeDict:
    pass

# instantiate class
fake_dict1 = FakeDict()
fake_dict2 = FakeDict()

# declare instance variables (instance = datatype)
fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This works too!"

# print output
working_string = "{}{}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string) 


# TEST 7: Instance Variables (Lesson)

class Store:
    pass

# instantiation
alternative_rocks = Store()
isabelles_ices = Store()

# intance variable
alternative_rocks.store_name = 'Alternative Rocks'
isabelles_ices.store_name = "Isabelle's Ices"

# consolidate variables
stores = "{}, {}".format(alternative_rocks.store_name, isabelles_ices.store_name)

print(stores)


# TEST 8: Notes
# * hasattr() -- returns True if oject has an attribute, False otherwise.

# * getattr() -- gets actual value of attribute. 

# TEST 8.1: Attribute Functions

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for i in can_we_count_it:
    if (hasattr(i, "count")):
        print(str(type(i)) + 'has the count attribute!')
    else:
        print(str(type(i)) + " does not have the count attribute.")

# TEST 9: Self Variable

class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2
  def circumference(self):
    return 2 * self.pi * self.radius

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(Circle.circumference(medium_pizza))
print(Circle.circumference(teaching_table))
print(Circle.circumference(round_room))

# TEST 10: Objects 

# OOP can be used to encapsulate functionality that process the input data with formatted output. 
# * dir()

class FakeDict:
    pass

fakedict = FakeDict()
fakedict.attribute = 'Cool'

print(dir(fakedict))


# TEST 11: Dunder Methods (__init__(), __repr__())

class Employee():
    def __init__(self, name):
        self.name = name

    def __repr__(self): #string representation
        return self.name

gil = Employee('Gil Horne Jr')
print(gil)

# TEST 12: Conclusion 

class Student:
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self, grade):
    self.grade = grade
    if type(grade) == Grade:
      self.grades.append(grade)
    else:
      pass
      

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score


roger = Student('Roger van der Weyden', 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8, )

grade1 = Grade(100)
pieter.add_grade(grade1)

# Write a Grade method .is_passing() that returns whether a Grade has a passing .score.

# Write a Student method .get_average() that returns the student’s average score.

# Add an instance variable to Student that is a dictionary called .attendance, with dates as keys and booleans as values that indicate whether the student attended school that day.