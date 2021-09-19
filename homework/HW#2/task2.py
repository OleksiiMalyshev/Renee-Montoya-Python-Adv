print('Task 2')
# 2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.
#   a.
#       class Person:
#           """
#           Make the class with composition.
#           """
#       class Arm:
#           """
#           Make the class with composition.
#           """
class Person:

    def __init__(self):
        left_arm = Arm("left")
        right_arm = Arm("right")
        self.arms = [left_arm, right_arm]


class Arm:

    def __init__(self, location):
        self.location = location


person = Person()
print(person.arms)
del person
print('\n')


# b.
#       class CellPhone:
#           """
#           Make the class with aggregation
#           """
#       class Screen:
#           """
#           Make the class with aggregation
#           """

class CellPhone:
    def __init__(self, screen):
        self.screen = screen

class Screen:
    def init(self):
        pass

screen = Screen()
cellphone = CellPhone(screen)

print(cellphone, screen)
del cellphone
print(screen)
