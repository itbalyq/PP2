def divisible_by_three_and_four_generator(N):
    for i in range(N+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

N = int(input("Enter a number: "))
for square in divisible_by_three_and_four_generator(N):
    print(square)
