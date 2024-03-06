filepath = r'C:\kbtu\pp2\labs\lab 6\dir_and_files\test.txt'

def count_lines(filepath):
    with open(filepath, 'r') as file:
        lines = 0
        for line in file:
            lines += 1
    
    return lines

print("Lines:", count_lines(filepath))