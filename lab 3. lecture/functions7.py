def word_frequency(string):
    words = string.split()

    frequency_dict = {}

    for word in words:
        if word in frequency_dict:
            frequency_dict[word] += 1
        else:
            frequency_dict[word] = 1

    return frequency_dict

text = "KBTU is is the best uni KBTU is in Kazakhstan Kazakhstan is best"

result = word_frequency(text)
print(result)