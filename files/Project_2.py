class School: 
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents

  def __repr__(self):
    return f'A {self.level} school named {self.name} with {self.numberOfStudents} students.'

  def get_name(self):
    return self.name

  def get_level(self):
    return self.level

  def get_numStudents(self):
    return self.numberOfStudents

  def set_numStudents(self, new_numStudents):
    self.numberOfStudents = new_numStudents


class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, 'primary', 300)
    self.pickupPolicy = pickupPolicy

  def __repr__(self):
    parentRepr = super().__repr__()
    return parentRepr + " The pickup policy is {pickupPolicy}".format(pickupPolicy = self.pickupPolicy)

  def get_pickup(self):
    return self.pickupPolicy
    

class HighSchool(School):
  def __init__(self,name, numberOfStudents, sportTeams):
    super().__init__(name, 'high', 500)
    self.sportTeams = sportTeams 

  def __repr__(self):
    parent_repr = super().__repr__()
    return parent_repr + f' Our sports teams are {self.sportTeams}'

  def get_sportTeams(self):
    return self.sportTeams

    
  
# TEST:
# a = School("Codecademy", "high", 100)
# print(a)
# print(a.get_name())
# print(a.get_level())
# a.set_numStudents(200)
# print(a.get_numStudents())

# b = PrimarySchool('Codecademy', 300, 'Pickup After 3pm')
# print(b)
# print(b.get_name())
# print(b.get_level())
# b.set_numStudents(400)
# print(b.get_numStudents())

c = HighSchool('Codecademy', 500, ['Tennis', 'Basketball', 'baseball'])
print(c.get_sportTeams())
print(c)