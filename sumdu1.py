import math
import time
import sys
import os

def calc(m):
    z = math.sqrt(int(m)) + 10
    return z

def average(x, y):
    x, y = int(x), int(y)
    nums = [num for num in range(x, y + 1) if num % 2 == 0]
    if not nums:
        return 0
    average_sum = sum(nums) / len(nums)
    return average_sum

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def effect(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main():
    effect("Enter num for func: ")
    m = input(">>> ")
    clear()
    if m.isdigit():
        effect(str(calc(m)))
    else:
        effect("Num is not integer")
    input("press enter to next >>>")
    clear()
    effect("Enter x: ")
    x = input(">>> ")
    clear()
    effect("Enter y: ")
    y = input(">>> ")
    clear()
    effect(f"average of (x and y): {average(x, y)}")
    input("press enter to stop >>>")
    clear()

if __name__ == "__main__":
    main()

