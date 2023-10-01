import sys
import copy

def static_test():
    _ = 100
    _ += 1
    return _

def main():
    print("Template For sample programs")
    d1 = dict(hour = 10, min = 20, sec = 13)
    print(d1)
    print(static_test())
    print(static_test())

    a = 3
    b = a
    print(f" a is {a}")
    print(f" b is {b}")
    a = "spam"
    print(f" a is {a}")
    print(f" b is {b}")

    a = [10, 20, 30, 40]
    b = list(a)
    a [1] = 100
    print(f"a is {a}")
    print(f"b is {b}")
    b = copy.copy(a)
    print(f"b is {b}")
          
if __name__ == "__main__":main()