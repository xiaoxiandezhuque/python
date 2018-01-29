#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

def checkio(text):
    text =text.lower()
    text=re.sub(r'[^a-z]+',"",text)

    count = 1
    str = text[0]

    for i in range(0, len(text)):
        t = text[i]
        t_count = 0
        for j in range(i, len(text)):
            if (text[j] == t):
                t_count += 1
        if (t_count >= count):
            count = t_count
            str = t
    print(str)
    print('----------------')
    return str


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
