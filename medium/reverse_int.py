import sys

x = int(sys.argv[1])

def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    abs_x = abs(x)
    reversed_x = sign * int(str(abs_x)[::-1])
    if reversed_x < -2**31 or reversed_x > 2**31 - 1:
        return 0
    return reversed_x
    
print(reverse(x))
