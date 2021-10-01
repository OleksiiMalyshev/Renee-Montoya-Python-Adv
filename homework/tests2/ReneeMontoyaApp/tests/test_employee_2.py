import unittest
from unittest.mock import patch

from models.models import Employee, Plant


class TestEmployee(unittest.TestCase):
    @patch('models.Plant.get_file_data')
    def setUp(self, plant_list_mock):
        plant_list_mock.return_value = [{"id": 1, "location": "Kiev", "name": "Alex", "director_id": 1},]
        self.plant = Plant.get_by_id(1)
        self.employee = Employee(1, 'Test', 'test@test.test', 'plant', 1)


    @patch('models.Plant.get_by_id')
    def test_department(self, plantMock):
        plantMock.return_value = self.plant
        self.assertEqual(self.employee.department(), self.plant)

    @patch('models.Plant.get_by_id')
    def test_department_2(self, mock_get_by_id):
        mock_get_by_id.return_value = None
        self.assertIsNone(self.employee.department(), self.plant)
