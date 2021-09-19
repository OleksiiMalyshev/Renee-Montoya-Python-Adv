print('Task 3')
# 3.
# class Profile:
#     """
#     Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
#     Override a printable string representation of Profile class and return: list of the params mentioned above
#     """

class Profile:
    def __init__(self, name, last_name, phone_number,
                 address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birhday = birthday
        self.age = age
        self.sex = sex
        self.lst = [name, last_name, phone_number,
                 address, email, birthday, age, sex]

    def __str__(self):
        return str(self.lst)

me = Profile('Alex','Mercer',5553535,'New York','a.mercer@bla.bla',
             '13.08',30,'male')
print(me)
