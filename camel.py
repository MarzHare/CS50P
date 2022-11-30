def main():
    camel = input("camelCase: ")
    print("snake_case: ", end="")
    snek(camel)
    print()

def snek(s):
    for c in s:
        if c.isupper():
            c = c.lower()
            print("_", end="")
        print(c, end="")
main()
