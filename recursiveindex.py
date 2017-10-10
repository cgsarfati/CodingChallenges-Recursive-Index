"""Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

For example:

    >>> recursive_index(5, [1, 3, 5, 2, 4])
    2

    >>> recursive_index("hey", ["hey", "there", "you"])
    0

    >>> recursive_index("you", ["hey", "there", "you"])
    2

    >>> recursive_index("zork", ["foo", "bar", "baz"]) is None
    True

"""


def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """

    # need to access index as int as a return value
    # need a counter for how many recursions we do (dictates next index)
    # if not found, return None

    # store idx as start_at
    def _recursive_index(needle, haystack, start_at):

        # BASE CASES
        # 1. Check if not found (we've gone too far)
        if start_at == len(haystack):
            return None

        # 2. Have we found it?
        if haystack[start_at] == needle:
            # return idx
            return start_at

        # PROGRESSION
        # increment idx by 1
        return _recursive_index(needle, haystack, start_at + 1)

    # start algorithm w/ idx 0
    return _recursive_index(needle, haystack, 0)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GO GO GO!\n"
