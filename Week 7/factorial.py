n = int(input("Enter the Superscribt >>> "))
r = int(input("Enter the subscript >>> "))


# FACTORIAL
def factorial(n):
    fac_list = 1
    i = 1
    while i <= n:
        fac_list *= i
        i += 1
    return fac_list


# PERMUTATION
def permutation(n, r):
    if r > n:
        print("Please crosscheck your input!!")
        pass
    else:
        numerator = factorial(n)
        denomerator = factorial(n - r)
        return numerator / denomerator



# COMBINATION
def combination(n, r):
    if r > n:
        print("Please crosscheck your input!!")
    else:
        numerator = factorial(n)
        denomerator = factorial(n - r) * factorial(r)
        return numerator / denomerator


class FacPerCom():
    
    def __init__(self):

        pass

    def factorial(self, n):
        fac_list = 1
        i = 1
        while i <= n:
            fac_list *= i
            i += 1
        return fac_list


    # PERMUTATION
    def permutation(self, n, r):
        if r > n:
            print("Please crosscheck your input!!")
            pass
        else:
            numerator = factorial(n)
            denomerator = factorial(n - r)
            return numerator / denomerator



    # COMBINATION
    def combination(self, n, r):
        if r > n:
            print("Please crosscheck your input!!")
        else:
            numerator = factorial(n)
            denomerator = factorial(n - r) * factorial(r)
            return numerator / denomerator


