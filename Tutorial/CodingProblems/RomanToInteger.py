
def romanToInt(s: str):
    # use dictionary to store key value pairs
    romanToInt = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # define variable for summarize of each charachter
    sum = 0

    # for loop until len(s) -1 because we can not compare last roman character to following value
    for i in range(len(s)-1):
        if romanToInt[s[i]] < romanToInt[s[i+1]]:
            sum = sum - romanToInt[s[i]]
        else:
            sum = sum + romanToInt[s[i]]

    # adding the last roman character to our sum
    return sum + romanToInt[s[-1]]

    # example: IV -> 4
    # romanToInt[s[I]] = 1 < romanToInt[s[V]] = 5
    # -> true -> sum = 0 -1 = -1
    # return -1 + 5 = 4

    # example 2: XV -> 15
    # romanToInt[s[X]] = 10 < romanToInt[s[V]] = 5
    # -> false -> sum = 0 + 10 = 10
    # return 10 + 5 = 15
