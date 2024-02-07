def calculate_running_average(numbers):
    running_sum = 0
    running_average_list = []

    for i, num in enumerate(numbers, start=1):
        running_sum += num
        running_average = running_sum / i
        running_average_list.append(running_average)

    return running_average_list

numbers_series = [1, 2, 3, 4, 5]
result = calculate_running_average(numbers_series)

print(f"Running average list: {result}")