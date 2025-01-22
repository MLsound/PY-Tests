from typing import Callable, Any

"""
    Making some tests with decorators, type anotation, high order functions, lambdas, map, filter
"""
def operator(funct: Callable, *args: Any) -> list[str] | int:
    return funct(*args)

def count(text: str) -> int:
    return len(text)

def letters(text: str) -> list[str]:
    list = []
    for char in text:
        list.append(char)
    return list

def vowels(text: str) -> int:
    vow = 0
    for char in text.lower():
        if char in {'a', 'e', 'i', 'o', 'u'}:
            vow += 1
    return vow

#==================================================

operations = [count,letters, vowels]
palindrome = lambda string: string == string[::-1]

names = ['ana','luis','juan','menem','john','ivi']

for name in names:
    if palindrome(name):
        print(name, "es un palindromo.")
        for op in operations:
            print(op.__name__, operator(op, name), sep=": ")
        print()
