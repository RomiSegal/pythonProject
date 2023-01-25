import os
from dotenv import load_dotenv
from datetime import datetime


class MyCar:
    load_dotenv()

    def __init__(self):
        self.km_per_liter = int(os.getenv('FUEL_KM'))
        self.gear_speed = int(os.getenv('GEAR_SPEED'))
        self.num_of_gear = int(os.getenv('NUM_OF_GEAR'))
        self.distance = int(os.getenv('DRIVE'))
        self.status = int(os.getenv('STATUS'))
        self.liter_for_km = int(os.getenv('LITER'))
        self.current_speed = int(os.getenv('CURRENT_SPEED'))
        self.capacity = int(os.getenv('CAPACITY'))
        self.money = int(os.getenv('MONEY'))
        self.current_fuel = int(os.getenv('CURRENT_FUEL'))

    def ready_for_drive(self, distance):
        '''
        name:Romi segal
        date:22/01
        The function tells if I can start driving or not
        :return: true if I can start to drive or false if not
        '''
        #Checking if I'm in drive mode and also have enough fuel for the distance I have to travel
        if self.is_enough_fuel(distance) and self.drive():
           self.write_to_log(os.getenv('READY_FOR_DRIVE_LOG'))
           return True
        else:
            return False

    def is_enough_fuel(self, distance):
        '''
        name:Romi segal
        date:22/01
        The function calculates if I have enough fuel for my trip
        :return:true if I have enough fuel or false if I have not
        '''
        #culc how much liter I can fill
        possible_liter = self.money // self.liter_for_km
        #Calculates the longest distance I can travel with the fuel I have
        possible_distance = (possible_liter + self.current_fuel) * self.km_per_liter

        #Checking if the desired distance is greater than the distance that is possible for me
        if distance > possible_distance:
            raise ValueError(os.getenv('IS_ENOUGH_FUEL_ERROR'))

        else:
            self.write_to_log(os.getenv('IS_ENOUGH_FUEL_LOG'))
            return True

    def fill_fuel(self, amount_of_liters):
        '''
        name:Romi segal
        date:22/01
        The function fills fuel according to the amount of fuel I received as a parameter and deducts from my money
        :param amount_of_liters:
        :return:
        '''
        try:
            free_liters = self.capacity - self.current_fuel
            #if I ask to fill more than I can
            if amount_of_liters > free_liters:
                amount_of_liters = free_liters
            needed_money = amount_of_liters * self.liter_for_km
            #if I have not enough money
            if self.money < needed_money:
                raise ValueError(os.getenv('FILL_FUEL_ERROR').format(needed_money-self.money))
            else:
                #current money
                self.money -= needed_money
                self.write_to_log(os.getenv('CURRENT_MONEY').format(amount_of_liters,self.money))
        except ValueError as e:
            self.write_to_log({e})

    def set_current_fuel(self,distance):
        '''
        name:Romi segal
        date:22/01
        The function calculator the current fuel after drive with this distance
        :param distance:
        :return:
        '''
        try:
            self.current_fuel -= distance / self.km_per_liter
        except ValueError as e:
            self.write_to_log({e})

    def total_speed(self):
        '''
        name:Romi segal
        date:22/01
        The function culc how much my total speed
        :return:total speed
        '''
        return self.gear_speed * self.status

    def write_to_log(self,str):
        """
         name :Romi Segal
         date : 18/01/2023
        function that appends the exceptions to a log file
         param str: string to write to the log
         return:
        """
        f = open(os.getenv('NAME_FILE'), 'a')
        f.write(f"\n{str} , {datetime.now()}")
        f.close()

    def drive(self):
        '''
        name:Romi segal
        date:22/01
        The function transfers from state stop to start
        :return:
        '''
        try:

            if self.status == 0:
                self.shift_up()
            else:
                raise Exception(os.getenv('DRIVE_ERROR'))
        except ValueError as e:
            self.write_to_log({e})

    def parking(self):
        '''
        name:Romi segal
        date:22/01
        The function transfers from state start to stop
        :return:
        '''
        try:
            if self.status > 0:
                self.status = 0
            else:
                raise Exception(os.getenv('PARKING_ERROR'))
        except ValueError as e:
            self.write_to_log({e})

    def get_current_fuel(self):
        return self.current_fuel

    def shift_up(self):
        '''
        name:Romi segal
        date:22/01
        The function moves up one gear
        :return:
        '''
        try:
            if self.status < self.num_of_gear:
                self.status += 1
            else:
                raise OverflowError(os.getenv('SHIFT_UP_ERROR'))
        except ValueError as e:
            self.write_to_log({e})

    def shift_down(self):
        '''
        name:Romi segal
        date:22/01
        The function lowers one gear
        :return:
        '''
        try:
            if not self.status < 0:
                self.status -= 1
            else:
                raise ValueError(os.getenv('SHIFT_DOWN_ERROR'))
        except ValueError as e:
            self.write_to_log({e})

