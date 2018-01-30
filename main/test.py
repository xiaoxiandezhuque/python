#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re

if __name__ == '__main__':
    text = set(['1', '2'])
    text.add("a")
    text = text | set(["aa", 'bb'])
    print(text)
