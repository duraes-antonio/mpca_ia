import numpy as np

def main():
    a: Set[int] = {1, 2}
    print(a)
    num = [1, 2, 3, 4, 5, 6, 7, 8]
    print([n for n in num if n % 2 == 0])
    return 0

main()