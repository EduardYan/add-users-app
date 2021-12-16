"""
This module have the class User
for create and have a model of user.
"""

class User:
  def __init__(self, name, age, description):
    # initials values for the user
    self.name = name
    self.age = age
    self.description = description


  def __str__(self) -> str:
      return f'This is a user with name {self.name}, age {self.age} and desciption {self.description}.'