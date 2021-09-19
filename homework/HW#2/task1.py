# 1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
# create an instance for each of the animal and call the unique method for it.
# Determine if each of the animal is an instance of the Animals class
#
# class Animals:
#     """
#     Parent class, should have eat, sleep
#     """
#
# class Animal1(Animal):
#     """
#     Some of the animal with 1-2 extra methods related to this animal
#     """
#
#
print('________________________________________________')
print('Task 1')


class Animals:

    def eat(self):
        print("Animal: Eating")

    def sleep(self):
        print("Animal: Sleeping")


class Wolf(Animals):
    def hunt(self):
        print("Wolf: Hunting with red eyes")


class Rabbit(Animals):
    def run(self):
        print("Rabbit: Run for your life")


class Pig(Animals):
    def dirt(self):
        print("Pig: I love dirt")


class Owl(Animals):
    def night_hunt(self):
        print("Owl: Love grizunov")


class Bear(Animals):
    def honey(self):
        print("Bear: I love honey")


wolf = Wolf()
wolf.eat()
wolf.sleep()
wolf.hunt()
print('\n')
rabbit = Rabbit()
rabbit.eat()
rabbit.sleep()
rabbit.run()
print('\n')
pig = Pig()
pig.eat()
pig.sleep()
pig.dirt()
print('\n')
owl = Owl()
owl.eat()
owl.sleep()
owl.night_hunt()
print('\n')
bear = Bear()
bear.eat()
bear.sleep()
bear.honey()
print('\n')


# 1.a.Create a new class Human and use multiple inheritance to
# create Centaur class, create an instance of Centaur
# class and call the common method of these classes and unique.
# class Human:
#     """
#     Human class, should have eat, sleep, study, work
#     """
#     """
#     Centaur class should be inherited from Human and Animal and has unique method related to it.
#     """
# class Centaur(.., ..):
#     pass

class Human():
    def think(self):
        print('Human: I can think!')


class Centaurus(Animals, Human):
    def horse_n_human(self):
        print('Centaur: I am human and horse at the same time')


human = Human()
human.think()
print('\n')
centaur = Centaurus()
centaur.eat()
centaur.sleep()
centaur.think()
centaur.horse_n_human()