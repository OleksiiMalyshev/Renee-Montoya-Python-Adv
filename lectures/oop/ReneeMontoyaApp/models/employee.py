from framework.models import Model


class Employee(Model):
    file = "employees.json"

    def __init__(self, id, name, email, department_type, department_id):
        self.id = id
        self.name = name
        self.email = email
        self.department_type = department_type
        self.department_id = department_id

    @classmethod
    def search_by_email(cls, email):
        for employee in cls.get_all():
            if employee.email == email:
                return employee
        raise Exception('No employee with such email')


    def __str__(self):
        return f'Emp(id={self.id}, email={self.email}, name={self.name}, ' \
               f'dep_type={self.department_type} dep_id={self.department_id})'
