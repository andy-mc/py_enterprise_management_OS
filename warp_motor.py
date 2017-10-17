#!/usr/bin/python

import sys


def get_operating_time(injector_capacity, injector_capacity_balance):
    '''Return the time the warp motor would be operational'''

    if injector_capacity_balance <= 0:
        return 'infinite'

    return injector_capacity - injector_capacity_balance


def motor_warp(a_injector_damage, b_injector_damage, c_injector_damage,
               speed_of_light_percentage):
    
    motor_capacity = 300
    injector_capacity = 100
    injector_extra_capacity = 99

    total_plasma_required = motor_capacity * (speed_of_light_percentage/100.0)

    a_injector_capacity = injector_capacity - (injector_capacity * a_injector_damage/100)
    b_injector_capacity = injector_capacity - (injector_capacity * b_injector_damage/100)
    c_injector_capacity = injector_capacity - (injector_capacity * c_injector_damage/100)

    motor_injectors = [a_injector_capacity, b_injector_capacity, c_injector_capacity]

    actual_motor_plasma_capacity = sum(motor_injectors)

    motor_plasma_balance = total_plasma_required - actual_motor_plasma_capacity

    avaiable_motor_injectors = sum([injector > 0 for injector in motor_injectors])
    injector_capacity_balance = motor_plasma_balance / avaiable_motor_injectors

    if injector_capacity_balance > injector_extra_capacity:
        return 'Unable to comply', 0

    operating_time = get_operating_time(injector_capacity, injector_capacity_balance)

    motor_injectors = [injector + injector_capacity_balance 
                       if injector > 0 else 0 for injector in motor_injectors]
    
    return motor_injectors, operating_time


def main():

    print('\n<< Welcome to the Enterprise warp motor OS >>\n')

    while True:
        print('Please enter the requested data below:')
        print('You can exit at any time pressing ^C or ^D\n')
        try:
            a_injector_damage = input('A injector damage: ')
            b_injector_damage = input('B injector damage: ')
            c_injector_damage = input('C injector damage: ')
            speed_of_light_percentage = input('Percentage of the speed of light: ')

        except (KeyboardInterrupt, EOFError):
            print('\n\nBye, bye see you soon...\n')
            sys.exit(0)

        motor_injectors, operating_time = motor_warp(a_injector_damage, b_injector_damage,
                                                     c_injector_damage, speed_of_light_percentage)

        print '\nYour results are:'
        if operating_time == 0:
            print '{}, Time: {} min.\n'.format(motor_injectors, operating_time)
        else:    
            print 'A: {} mg/s, B: {} mg/s, C: {} mg/s, Time: {} min.\n'.format(motor_injectors[0], motor_injectors[1], motor_injectors[2], operating_time)



if __name__ == '__main__':
    main()
