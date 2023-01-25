import unittest
import os
from dotenv import load_dotenv
from Car.my_car import MyCar


class TestMyCar(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.car = MyCar()

    def test_start(self):
        '''
        name:Romi Segal
        date:22/01
        The test checks if after I switch to drive mode and shift up if it is equal to second gear
        :param car:
        :return:
        '''
        try:
            self.car.drive()
            self.car.shift_up()
            self.assertEqual(self.car.status, 2)
            self.car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_start'))
        except AssertionError as err:
            self.car.write_to_log(os.getenv('TEST_ERROR').format('test_start',err))


    def test_parking1(self):
        '''
        name:Romi Segal
        date:22/01
        The test checks if after I switch to drive mode and downshift if the gear is equal to zero
        :param car:
        :return:
        '''
        try:
            self.car.drive()
            self.car.shift_down()
            self.assertEqual(self.car.status, 0)
            self.car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_parking1'))
        except AssertionError as err:
            self.car.write_to_log(os.getenv('TEST_ERROR').format('test_parking1',err))

    def test_parking2(self):
        '''
        name:Romi Segal
        date:22/01
        The test checks if after I switch to drive mode and return to parking if the gear is equal to zero
        :param car:
        :return:
        '''
        try:
            self.car.drive()
            self.car.parking()
            self.assertEqual(self.car.status, 0)
            self.car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_parking2'))
        except AssertionError as err:
            self.car.write_to_log(os.getenv('TEST_ERROR').format('test_parking2',err))

    def test_max_gear(self):
        '''
        name:Romi Segal
        date:22/01
        The test checks for boundary values , it raises a gear up to
         its limit and then catches it as it crosses the limit
        :param car:
        :return:
        '''
        try:
            for i in range(self.car.num_of_gear):
                self.car.shift_up()
            self.assertRaises(OverflowError, self.car.shift_up)
            self.car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_max_gear'))
        except AssertionError as err:
            self.car.write_to_log(os.getenv('TEST_ERROR').format('test_max_gear',err))

    def test_is_enough_fuel1(self):
        '''
        name:Romi Segal
        date:22/01
        The test checks if there is enough fuel in the car to start driving
         according to the number of kilometers I gave (400)
        :param car:
        :return:
        '''
        try:
            self.assertEqual(self.car.is_enough_fuel(400), True)
            self.car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_is_enough_fuel1'))
        except AssertionError as err:
            self.car.write_to_log(os.getenv('TEST_ERROR').format('test_is_enough_fuel1',err))

    def test_is_enough_fuel2(self):
        '''
        name:Romi Segal
        date:22/01
        The test checks if there is enough fuel in the car to start driving with
         an abnormal number of kilometers and the test is carried out without exception because the test catches it
        :param car:
        :return:
        '''
        try:
            self.assertRaises(ValueError, self.car.is_enough_fuel, 3000)
            self.car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_parking2'))
        except AssertionError as err:
            self.car.write_to_log(os.getenv('TEST_ERROR').format('test_parking2',err))

    def test_money_after_fill_fuel1(self):
        '''
        name:Romi Segal
        date:22/01
        The test checks how much money you have left after refueling
        :param car:
        :return:
        '''
        try:
            self.car.set_current_fuel(100)
            self.car.fill_fuel(5)
            self.assertEqual(self.car.money, 450)
            self.car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_fill_fuel1'))
        except AssertionError as err:
            self.car.write_to_log(os.getenv('TEST_ERROR').format('test_fill_fuel1',err))

    def test_money_after_fill_fuel2(self):
        '''
        name:Romi Segal
        date:22/01
        The test checks how much money you have left after refueling
        :param car:
        :return:
        '''
        try:
            self.car.set_current_fuel(200)
            self.car.fill_fuel(10)
            self.assertEqual(self.car.money, 400)
            self.car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_fill_fuel2'))
        except AssertionError as err:
            self.car.write_to_log(os.getenv('TEST_ERROR').format('test_fill_fuel2',err))

    def test_total_speed1(self):
        '''
        name:Romi Segal
        date:22/01
        The test checks your total speed
        :param car:
        :return:
        '''
        try:
            speed = self.car.total_speed()
            self.assertEqual(speed, 0)
            self.car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_total_speed1'))
        except AssertionError as err:
            self.car.write_to_log(os.getenv('TEST_ERROR').format('test_total_speed1',err))

    def test_total_speed2(self):
        '''
        name:Romi Segal
        date:22/01
        The test checks your total speed
        :param car:
        :return:
        '''
        try:
            self.car.drive()
            self.car.shift_up()
            speed = self.car.total_speed()
            self.assertEqual(speed, 60)
            self.car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_total_speed2'))
        except AssertionError as err:
            self.car.write_to_log(os.getenv('TEST_ERROR').format('test_total_speed2',err))

    def test_set_current_fuel1(self):
        '''
        name:Romi Segal
        date:22/01
        The test checks if after driving 200 kilometers it updates the fuel tank to 40
        :param car:
        :return:
        '''
        try:
            self.car.set_current_fuel(200)
            self.assertEqual(self.car.get_current_fuel(), 40)
            self.car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_set_current_fuel1'))
        except AssertionError as err:
            self.car.write_to_log(os.getenv('TEST_ERROR').format('test_set_current_fuel1',err))

    def test_set_current_fuel2(self):
        '''
        name:Romi Segal
        date:22/01
        The test checks if after driving 300 kilometers it updates the fuel tank to 35
        :param car:
        :return:
        '''
        try:
            self.car.set_current_fuel(300)
            self.assertEqual(self.car.get_current_fuel(), 40)
            self.car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_set_current_fuel2'))
        except AssertionError as err:
            self.car.write_to_log(os.getenv('TEST_ERROR').format('test_set_current_fuel2',err))

if __name__ == '__main__':
    unittest.main()
