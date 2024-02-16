def squares_generator(N):
    for i in range(N):
        yield i**2


N = int(input("Enter a number: "))
for square in squares_generator(N):
    print(square)

