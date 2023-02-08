# Check if a given number is a prime number or not.
# Return True or False depending on the result

from math import sqrt


def main(num: int):
    # prime number has to be >1
    if num == 1:
        return False
    elif num > 1:
        for i in range(2, int(sqrt(num)) + 1):
            if (num % i) == 0:
                return False
        return True


if __name__ == "__main__":
    main()
