import re
zen = """Although never is
often better than
*right* now.
If the implementation
is hard to explain,
it's a bad idea.
If the implementation
is easy to explain,
it may be a good
idea. Namespaces
are one honking
great idea -- let's
do more of those!
"""

m = re.findall("^If", zen, re.MULTILINE)
print(m)

string = "Two too."

f = re.findall("t[ow]o", string, re.IGNORECASE)
print(f)

line = "123?34 hello?"

fm = re.findall("\d", line, re.IGNORECASE)
print(fm)

t = "__one__ __two__ __three__"
found = re.findall("__.*?__", t)

for match in found:
    print(match)

line = "I love $"

li = re.findall("\\$",
                line,
                re.IGNORECASE)
print(li)
