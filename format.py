#!/usr/bin/env python3

# Created by: Huzaifa Khalid
# Created on: April 2022
# This program shows formatting output


def main():
    # this function uses a while loop
    loop_counter = 0
    total = 0

    # input
    user_number_as_string = int(input("Enter a positive integer: "))
    print("")
    # process & output
    try:
        user_number_as_integer = int(user_number_as_string)
        while loop_counter < user_number_as_integer:
            loop_counter = loop_counter + 1
            total = total + loop_counter
        print("The sum of is {0}".format(total))
    except Exception:
        print("¯\_(ツ)_/¯ sorry fam not an integer.")
    print("\nDone.")


if __name__ == "__main__":
    main()
