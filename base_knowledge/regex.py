# -*- coding: utf-8 -*-  
# Author: bellawu
# Date: 2021/2/17 21:12
# File: regex.py
# IDE: PyCharm

import re

# matching string
name1 = 'bella'
name2 = 'Quella'
sentence = 'Bella and Quella are the best sisters!'
print(name1 in sentence)
print(name2 in sentence)

# regular expression
print(re.search(name1, sentence))
print(re.search(name2, sentence))

# multiple patterns
names = r"[BQu]ella"
print(re.search(names, sentence))

# \d : decimal digit
print(re.search(r"r\dn", "run r4n"))
# \D : any non-decimal digit
print(re.search(r"r\Dn", "run r4n"))

# \s : any white space [\t\n\r\f\v]
print(re.search(r"r\sn", "r\nn r4n"))
# \S : opposite to \s, any non-white space
print(re.search(r"r\Sn", "r\nn r4n"))

# \w : [a-zA-Z0-9_]
print(re.search(r"r\wn", "r\nn r4n"))
# \W : opposite to \w
print(re.search(r"r\Wn", "r\nn r4n"))

# \b : empty string (only at the start or end of the word)
print(re.search(r"\bruns\b", "dog runs to cat"))
# \B : empty string (but not at the start or end of a word)
print(re.search(r"\B runs \B", "dog   runs  to cat"))

# \\ : match \
print(re.search(r"runs\\", "runs\ to me"))
# . : match anything (except \n)
print(re.search(r"r.n", "r[ns to me"))

# ^ : match line beginning
print(re.search(r"^dog", "dog runs to cat"))
# $ : match line ending
print(re.search(r"cat$", "dog runs to cat"))

# ? : may or may not occur
print(re.search(r"Mon(day)?", "Monday"))
print(re.search(r"Mon(day)?", "Mon"))

# multi-line
string = """
dog runs to cat.
I run to dog.
"""
print(re.search(r"^I", string))
print(re.search(r"^I", string, flags=re.M))

# * : occur 0 or more times
print(re.search(r"ab*", "a"))
print(re.search(r"ab*", "abbbbb"))

# group
match = re.search(r"(\d+), Date: (.+)", "ID: 021523, Date: Feb/12/2017")
print(match.group())
print(match.group(1))
print(match.group(2))
match = re.search(r"(?P<id>\d+), Date: (?P<date>.+)", "ID: 021523, Date: Feb/12/2017")
print(match.group('id'))
print(match.group('date'))

# findall
print(re.findall(r"r[ua]n", "run ran ren"))

# | : or
print(re.findall(r"(run|ran)", "run ran ren"))

# re.sub() replace
print(re.sub(r"r[au]ns", "catches", "dog runs to cat"))

# re.split()
print(re.split(r"[,;\.]", "a;b,c.d;e"))

# compile 先将正则编译进一个变量，然后直接用变量来进行正则搜索
compiled_re = re.compile(r"r[ua]n")
print(compiled_re.search("dog ran to cat"))
