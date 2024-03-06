import os

directory_path = "/kbtu/pp2/labs/lab 6/dir_and_files/6"

for i in range(26):
    filename = os.path.join(directory_path, f"{chr(ord('A') + i)}.txt")
    with open(filename, "w") as file:
        file.write("")

print("Finished!")