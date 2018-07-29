""" Lab 3: Recursion and Python Lists """

# Q1
def skip_add(n, sum=0):
    """ Takes a number x and returns x + x-2 + x-4 + x-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> check('lab03.py', 'skip_add',
    ...       ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 1:
      return sum
    n, sum = n - 2, sum + n
    return skip_add(n, sum)

def is_even(num):
    return n % 2 == 0

# Q2
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> # Do not use while/for loops!
    >>> from construct_check import check
    >>> check('lab03.py', 'hailstone',
    ...       ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n == 1:
        print(1)
    elif is_even(n):
        new_num = n / 2
        print(new_num)
        return hailstone(new_num)
    else:
        new_num = n * 2 + 1
        print(new_num)
        return hailstone(new_num)

# Q3
def if_this_not_that(i_list, this):
    """Define a function which takes a list of integers `i_list` and an integer
    `this`. For each element in `i_list`, print the element if it is larger
    than `this`; otherwise, print the word "that".

    >>> original_list = [1, 2, 3, 4, 5]
    >>> if_this_not_that(original_list, 3)
    that
    that
    that
    4
    5
    """
    "*** YOUR CODE HERE ***"
    for num in i_list:
        if num > this:
            print(num)
        else:
            print('that')
