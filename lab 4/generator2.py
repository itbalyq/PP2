def even_numbers_generator(n):
    for i in range(n+1):
        if i % 2 == 0:
            yield i

n = int(input("Enter a number: "))
even_numbers = list(even_numbers_generator(n))
print(even_numbers)