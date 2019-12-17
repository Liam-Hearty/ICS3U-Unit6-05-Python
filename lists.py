#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: Dec 2019
# This program finds the average of a bunch of numbers.


def adding_list(numbers):
    # This function adds all numbers

    total = 0
    counter = 0

    for counter in range(0, len(numbers)):
        total = total + numbers[counter]
        counter += 1
    total = total / len(numbers)

    return total


def main():
    # this function uses a list

    numbers = []
    # single_num = 0
    counter = 0

    # input
    print("Please enter a whole number from 0-100 repeatedly.")
    print("Enter a number lower then 0 or heigher then 100 to end.")

    single_num = int(input("Enter a number: "))
    numbers.append(single_num)
    while numbers[counter] > 0 and numbers[counter] <= 100:
        try:
            single_num = int(input("Enter a number: "))
        except(ValueError):
            print("Please input a proper number.")
        numbers.append(single_num)
        counter += 1

    numbers.pop()  # remove the "-1" that was added
    print("")

    total = adding_list(numbers)

    print("The average is {0}.".format(round(total)))


if __name__ == "__main__":
    main()
