def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def main():
    a, b = 1, 2
    print(f"{a}と{b}を足すと{add(a, b)}です。")
    print(f"{b}から{a}を引くと{sub(b, a)}です。")

if __name__ == '__main__':
    main()
