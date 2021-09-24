from models.plant import Plant
from models.employee import Employee


class Controller:

    def __init__(self, flag=0):
        self.flag = flag

    def choise(self):
        self.flag = int(input("Choose a menu item by number: \n" +
              "1. Add new Plant \n" +
              "2. Add new Employee \n" +
              "3. Get plant by id \n" +
              "4. Get employee by id \n"))
        if self.flag == 1:
            self.flag_1()
        elif self.flag == 2:
            self.flag_2()
        elif self.flag == 3:
            self.flag_3()
        elif self.flag == 4:
            self.flag_4()

    def flag_1(self):
        try:
            id = int(input("ID: "))
        except ValueError:
            print('Put the number!')
            return
        try:
            plant = Plant.get_by_id(id)
            print(f"Plant with id {id} and name {plant['name']} already exists")
        except Exception as _:
            location = input("Location: ")
            name = input("Name: ")
            email = input("Director email: ")
            try:
                emp = Employee.search_by_email(email)
            except Exception as _:
                print('Email not found')
                return
            plant = Plant(id, location, name, emp.id)
            plant.save()

    def flag_2(self):
        id = int(input("ID: "))
        name = input("Name: ")
        email = input("Email: ")
        department_type = input("Department Type: ")
        department_id = int(input("Department id: "))
        employee = Employee(id, name, email, department_type, department_id)
        employee.save()

    def flag_3(self):
        id = int(input("ID: "))
        plant = Plant.get_by_id(id)
        print(plant)

    def flag_4(self):
        id = int(input("ID: "))
        employee = Employee.get_by_id(id)
        print(employee)


