from math import sqrt
a=5
def main(a):
    """
    Check that the number "a" is a perfect square.
    Args:
        a: int
    Returns:
        bool
    """
    # Write your code here
    return sqrt(a)%1==0
print(main(a))