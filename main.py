from Car import my_car

if __name__ == '__main__':
    car = my_car.MyCar()

try:
    car.ready_for_drive(400)
    car.set_current_fuel(100)
    car.fill_fuel(5)

except ValueError as e:
        car.write_to_log(e)
        print(e)
except Exception as e:
        car.write_to_log(e)
        print(e)
