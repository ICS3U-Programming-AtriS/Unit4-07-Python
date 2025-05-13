#!/usr/bin/env python3
# Created By: Atri Sarker
# Date: May 13, 2025
# Program that prints the integers from 1000 to 2000


def main():
    # Loop through all integers from 1000 to 2000, inclusive
    for num in range(1000, 2001):
        # Print the number
        print(num, end=" ")
        # Check if number is the last number in the row
        if (num + 1) % 5 == 0:
            # If it is, print a newline
            print()
    # Print a newline at the end to close off the output
    print()


if __name__ == "__main__":
    main()
