import pytest
import os
from dotenv import load_dotenv
from Car.my_car import MyCar


@pytest.fixture
def car():
    load_dotenv()
    return MyCar()


def test_start(car):
    '''
    name:Romi Segal
    date:22/01
    The test checks if after I switch to drive mode and upshift if it is equal to second gear
    :param car:
    :return:
    '''
    try:
        car.drive()
        car.shift_up()
        assert car.status == 1
        car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_start'))
    except AssertionError as err:
        car.write_to_log(os.getenv('TEST_ERROR').format('test_start',err))


@pytest.mark.one
def test_parking1(car):
    '''
    name:Romi Segal
    date:22/01
    The test checks if after I switch to drive mode and downshift if the gear is equal to zero
    :param car:
    :return:
    '''
    try:
        car.drive() #up one
        car.shift_down() #down one
        assert car.status == 0
        car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_parking1'))
    except AssertionError as err:
        car.write_to_log(os.getenv('TEST_ERROR').format('test_parking1',err))


@pytest.mark.two
def test_parking2(car):
    '''
    name:Romi Segal
    date:22/01
    The test checks if after I switch to drive mode and return to parking if the gear is equal to zero
    :param car:
    :return:
    '''
    try:
        car.drive()
        car.parking()
        assert car.status == 0
        car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_parking2'))
    except AssertionError as err:
        car.write_to_log(os.getenv('TEST_ERROR').format('test_parking2',err))

@pytest.mark.three
def test_max_gear(car):
    '''
    name:Romi Segal
    date:22/01
    The test checks for boundary values , it raises a gear up to
     its limit and then catches it as it crosses the limit
    :param car:
    :return:
    '''
    try:
        for i in range(car.num_of_gear):
            car.shift_up()
            print(i)
        with pytest.raises(OverflowError):
            car.shift_up()
            car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_max_gear'))
    except AssertionError as err:
        car.write_to_log(os.getenv('TEST_ERROR').format('test_max_gear',err))

@pytest.mark.four
def test_is_enough_fuel1(car):
    '''
    name:Romi Segal
    date:22/01
    The test checks if there is enough fuel in the car to start driving
     according to the number of kilometers I gave (400)
    :param car:
    :return:
    '''
    try:
        assert car.is_enough_fuel(400) == True
        car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_is_enough_fuel1'))
    except AssertionError as err:
        car.write_to_log(os.getenv('TEST_ERROR').format('test_is_enough_fuel1',err))


def test_is_enough_fuel2(car):
    '''
    name:Romi Segal
    date:22/01
    The test checks if there is enough fuel in the car to start driving with
     an abnormal number of kilometers and the test is carried out without exception because the test catches it
    :param car:
    :return:
    '''
    try:
        with pytest.raises(ValueError):
            car.is_enough_fuel(3000)
            car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_is_enough_fuel2'))
    except AssertionError as err:
        car.write_to_log(os.getenv('TEST_ERROR').format('test_is_enough_fuel2',err))

def test_money_after_fill_fuel1(car):
    '''
    name:Romi Segal
    date:22/01
    The test checks how much money you have left after refueling
    :param car:
    :return:
    '''
    try:
        car.set_current_fuel(100)
        car.fill_fuel(5)
        assert car.money == 450
        car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_fill_fuel1'))
    except AssertionError as err:
        car.write_to_log(os.getenv('TEST_ERROR').format('test_fill_fuel1',err))

def test_money_after_fill_fuel2(car):
    '''
    name:Romi Segal
    date:22/01
    The test checks how much money you have left after refueling
    :param car:
    :return:
    '''
    try:
        car.set_current_fuel(200)
        car.fill_fuel(10)
        assert car.money == 400
        car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_fill_fuel2'))
    except AssertionError as err:
        car.write_to_log(os.getenv('TEST_ERROR').format('test_fill_fuel2',err))

def test_total_speed1(car):
    '''
    name:Romi Segal
    date:22/01
    The test checks your total speed
    :param car:
    :return:
    '''
    try:
        car.total_speed()
        assert car.total_speed() == 0
        car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_total_speed1'))
    except AssertionError as err:
        car.write_to_log(os.getenv('TEST_ERROR').format('test_total_speed1',err))

def test_total_speed2(car):
    '''
    name:Romi Segal
    date:22/01
    The test checks the speed after I switched to drive mode and raised a gear
    :param car:
    :return:
    '''
    try:
        car.drive()
        car.shift_up()
        car.total_speed()
        assert car.total_speed() == 60
        car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_total_speed2'))
    except AssertionError as err:
        car.write_to_log(os.getenv('TEST_ERROR').format('test_total_speed2',err))

def test_set_current_fuel1(car):
    '''
    name:Romi Segal
    date:22/01
    The test checks if after driving 200 kilometers it updates the fuel tank to 40
    :param car:
    :return:
    '''
    try:
        car.set_current_fuel(200)
        assert car.current_fuel == 40
        car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_set_current_fuel1'))
    except AssertionError as err:
        car.write_to_log(os.getenv('TEST_ERROR').format('test_set_current_fuel1',err))
def test_set_current_fuel2(car):
    '''
    name:Romi Segal
    date:22/01
    The test checks if after driving 300 kilometers it updates the fuel tank to 35
    :param car:
    :return:
    '''
    try:
        car.set_current_fuel(300)
        assert car.current_fuel == 35
        car.write_to_log(os.getenv('WRITE_TO_LOG').format('test_set_current_fuel2'))
    except AssertionError as err:
        car.write_to_log(os.getenv('TEST_ERROR').format('test_set_current_fuel2',err))