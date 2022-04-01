class Person:
  def __init__(self, name, last_name, birth_date):
    self.name = name
    self.last_name = last_name
    self.birth_date = birth_date


p1 = Person("John", "Dylan","May 24, 1941")

print("Name: " + p1.name)
print("Last name: " + p1.last_name)
print("Birth date: "+ p1.birth_date)