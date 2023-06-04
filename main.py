def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def main():
    a, b = 1, 2
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{b} - {a} = {sub(b, a)}")
    print(f"{a} * {b} = {mul(a, b)}")

if __name__ == '__main__':
    main()
