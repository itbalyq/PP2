file_path = r'C:\kbtu\pp2\labs\lab 5\row.txt'

with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()


import re

def first(text):
    x = re.findall(r"ab*", text)
    return x
#print(first(text))

def second(text):
    x = re.findall(r"ab{2,3}", text)
    return x
#print(second(text))

def third(text):
    x = re.findall(r'\b[a-z]+_[a-z]+\b', text)
    return x
#print(third(text))


def fourth(text):
    x = re.findall(r'\b[A-Z][a-z]+\b', text)
    return x
#print(fourth(text))


def fifth(text):
    x = re.findall(r'\ba\w*b\b', text)
    return x
print(fifth(text))


def sixth(text):
    pattern = r'[ ,.]'
    x = re.sub(pattern, ":", text)
    return x
#print(sixth(text))


str = "turn_into_camel"
def seventh(text):
    return re.sub(r'_([a-z])', lambda x: x.group(1).upper(), text) 
#print(seventh(str))


def eigth(text):
    return re.findall(r'[A-ZА-Я][a-zа-я]*', text)
#print(eigth(text))


def ninth(text):
    return re.sub(r'([a-z])([A-Z])', r'\1 \2', text)          
#print(ninth("AnExampleToTesttheFunction"))

def tenth(text):
    return re.sub(r'([a-z])([A-Z])', r'\1_\2', text).lower() 
#print(tenth("AnExampleToTesttheFunction"))
