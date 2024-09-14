# ASSIGNMENT 1



# CUSTOM IMPORTS
import numpy as np


# USER INTERFACE




# MAIN CODE
def main():
    pass
#


def find_median(*args):
    mde = np.median(list(args))
    return mde
#

def check_prime(*args):
    primelst = []
    for ele in list(args):
        if ele == 1:
            primelst.append(ele)
        elif ele == 2:
            primelst.append(ele)
        else:
            prime_ = True
            for i_c in range(2, ele):
                if ele % i_c == 0:
                    prime_ = False
        if prime_:
            primelst.append(ele)
    #
    return print(f'The natural number/s {primelst} is/are a Prime')


a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
c = int(input('Enter 3rd number: '))
d = int(input('Enter 4th number: '))

uiop = check_prime(a,b,c,d)

print(f'The median is {find_median(a,b,c,d)}')
