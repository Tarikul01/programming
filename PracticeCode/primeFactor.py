def primeFactors(n):
    c = 2
    while (n > 1):

        if (n % c == 0):
            print(c, end=" ")
            n = n / c
        else:
            c = c + 1


# Driver code
n = 315
primeFactors(n)

# This code is contributed by Taranpreet