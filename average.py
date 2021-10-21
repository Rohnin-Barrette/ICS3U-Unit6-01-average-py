#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: oct 2021
# this function generates 10 random numbers and finds the average between them

import random


def main():
    # This function generates 10 random numbers and finds the average between them

    average = 0
    number_list = []
    total = 0

    # input
    for loop_counter in range(0, 10):
        random_number = random.randint(0, 100)
        total = total + random_number
        number_list.append(random_number)
        print("The random number is: {}".format(random_number))
    average = total / len(number_list)

    print("\nthe average is {}".format(average))
    print("\nDone.")


if __name__ == "__main__":
    main()
