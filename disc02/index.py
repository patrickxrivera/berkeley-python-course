def is_even(num):
  return num % 2 == 0

def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ... # Even numbers have remainder 0 when divided by 2.
    ... return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """

    [print(num) for num in range(1, n) if cond(num)]

def keep_ints(n):
    """Returns a function which takes one parameter cond and prints out
    all integers 1..i..n where calling cond(i) returns True.
    >>> def is_even(x):
    ... # Even numbers have remainder 0 when divided by 2.
    ... return x % 2 == 0
    >>> keep_ints(5)(is_even)
    2
    4
    """
    def fn(cond):
      [print(num) for num in range(1, n) if cond(num)]
    return fn

keep_ints(5)(is_even)
