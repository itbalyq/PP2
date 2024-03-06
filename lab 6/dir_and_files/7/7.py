buffer = ""

input_file = r'C:\kbtu\pp2\labs\lab 6\dir_and_files\7\input.txt'
output_file = r'C:\kbtu\pp2\labs\lab 6\dir_and_files\7\output.txt'

with open(input_file, "r") as file:
    buffer = file.read()

with open(output_file, "w") as file:
    file.write(buffer)
