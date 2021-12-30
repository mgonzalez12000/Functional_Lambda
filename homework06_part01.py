# Marco Gonzalez
# CS 3035 - 01

# Sources used to check correct output:
# https://prime-numbers.info/list/emirps
# https://prime-numbers.info/list/twin-primes

# CHANGES MADE UPON RESUBMISSION
# 1) Upon first submission, according to the cited source above, my emirps output was wrong.
# This is because my algorithm only took into account for one function name being passed.
# The fixed __call__ algorithm was updated to check if the list of function names takes
# in more than one function. This was done with a boolean value.
# 2) The other implemented functions were made to look more "pythonic" by writing if-else
# statements in one line. However, the logic for these if-else statements remain the same.

# Part 01 (1 point): For this problem you will generate lists of prime numbers
# given different sets of criteria.
#
# Create a callable object by implementing a class named CustomPrimes, the skeleton
# of which is given below.  In order to create a callable object, you must
# implement the __call__ method in the class. This method should be implemented
# as a GENERATOR and its job is to generate all prime numbers from 2 to n (inclusive)
# that fit the criteria of one or more boolean functions. The list of function
# names will be passed into the constructor for the CustomPrimes class.
# Assume that the number of functions passed, could be any number.  You may not hardcode
# the number of functions.

# For this problem you do not need to use recursion as recursion can make this
# crash in python.  If you would like to use recursion for any of the boolean
# methods where the depth of recursion isn't too great feel free.

# Please see the comments given for the rest of the directions.

class CustomPrimes():
    def __init__(self, functions):
        self.functions = functions

    def __call__(self, n):
        # YOU IMPLEMENT THIS FUNCTION
        # This function should generate all primes that fit the conditions
        # given by each of the functions passed to the constructor. Implement
        # this as a generator.

        for i in range(2, n + 1):
            one_function: bool = True
            for functs in self.functions:
                result = functs
                if is_prime(i) == True and result(i) == False:
                    one_function = False
                else:
                    continue
            if is_prime(i) and one_function:
                yield i


# The following functions are the boolean functions that will be passed into
# the constructor of the class.  Not all functions will be passed all the time.

# USE THIS FUNCTION AS IT IS
# This function returns true if p is prime, false otherwise.
# NOTE: If you find a better implementation of finding out if a number is prime
# or not, feel free to use it and let me know about it!
def is_prime(p):
    return [x for x in range(1, p + 1) if p % x == 0] == [1, p]


def is_palindrome(p):
    # YOU IMPLEMENT THIS FUNCTION
    # This function should return true if p is a palindrome, false if not.
    # p is a palindrome if it is the same value forwards and backwards.
    # NOTE: single digit numbers are considered to be palindromes.
    return str(p) == str(p)[::-1]


def is_not_palindrome(p):
    # YOU IMPLEMENT THIS FUNCTION
    # This function should return true if p is not a palindrome, false otherwise.

    return True if not is_palindrome(p) else False


def is_reverse_prime(p):
    # YOU IMPLEMENT THIS FUNCTION
    # # This function should return true if the reverse of p is prime, false otherwise.

    return True if is_prime(int(str(p)[::-1])) else False


def is_twin_prime(p):
    # YOU IMPLEMENT THIS FUNCTION
    # This function should return true if p is part of a set of twin primes, false otherwise
    # p is part of a set of twin primes if p+2 is prime or p-2 is prime.
    # also prime.

    return True if is_prime(p + 2) or is_prime(p - 2) else False


def main():
    # In your main method you should generate the following types of prime numbers
    # using instances of your callable object class CustomPrimes.  For all lists
    # please demonstrate that your code works when N = 10000

    # Show all palindromic primes from 2 to 10000.  A number is a palindromic prime
    # if it is a prime number and also a palindrome.

    palindromic_primes = CustomPrimes([is_palindrome])
    print('Palindromic primes:', list(palindromic_primes(10000)))

    # Show all emirps. An emirp is a nonpalindromic prime number whose
    # reversal is also prime.

    emirps = CustomPrimes([is_not_palindrome, is_reverse_prime])
    print('Emirps:', list(emirps(10000)))

    # Show all twin primes.  Twin primes are pairs of prime numbers that differ by 2.
    # Example, 3 and 5 are twin primes, 5 and 7 are twin primes, 11 and 13 are twin primes
    # and so on.

    twin_primes = CustomPrimes([is_twin_prime])
    print('Twin primes:', list(twin_primes(10000)))

    # please display your output in a nice format.


if __name__ == "__main__":
    main()
