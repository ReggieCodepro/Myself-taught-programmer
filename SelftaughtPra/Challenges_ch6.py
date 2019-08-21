#Challenge 1
Char = "Camus"
print(Char[0])
print(Char[1])
print(Char[2])
print(Char[3])
print(Char[4])

#Challenge 2
R1 = input("Enter a response:")
R2 = input("Enter a response:")

R3 = "Yesturday I wrote a {}. I sent it to {}" .format(R1, R2)
print(R3)

#Challenge 3
Capliz = "aldous Huxley was born in 1894." .capitalize()
print(Capliz)

#Challenge 4
lst = "where now? Who now? When now?" .split("?")
print(lst)

#Challenge 5
words = ("The", "fox", "jumped", "over", "the", "fence", ".")
words = " " .join(words)
words = words[0: -2] + "."
print(words)

#Challenge 6
ReRe = "A screaming comes across the sky."
ReRe = ReRe.replace("s", "$")
print(ReRe)

#Challenge 7
find = "Hemingway" .index("m")
print(find)

#Challenge 8
qoute = 'she look at me and said "I want the D now"'
qoute2 = 'I wanted nothing to do with a her fat ass so I replied "Hell no, you got a man and you got four kids"'
print(qoute, qoute2)
#Challenge 9
Three = "threethreethree"
Three1 = "three" + " ", "three" + " ", "three"
Three2 = "three " * 3
print(Three1)
print(Three2)

#Challenge 10
only = "It was a bright cold day in April, and the clocks were striking thirteen."
new = only[:33]
print(new)









