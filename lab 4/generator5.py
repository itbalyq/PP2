def countdown_generator(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter a number: "))
for square in countdown_generator(n):
    print(square)
