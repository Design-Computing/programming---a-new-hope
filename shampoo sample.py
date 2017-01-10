import string


def makeShampoo(word):
    if word == "cook":
        return "Shampoo"
    else:
        return word


def halCode(letter):
    a = list(string.ascii_lowercase)
    b = a[1:] + a[:1]
    c = zip(a, b)
    d = dict(c)
    d[" "] = "*"
    return d[letter.lower()]


phrase = "I asked you to cook the egg"
words = phrase.split(" ")
newWords = map(makeShampoo, words)
newPhrase = " ".join(newWords)

print "phrase:", phrase
print "words:", words
print "newWords:", newWords
print "newPhrase", newPhrase

print "".join(map(halCode, "IBM"))

a = "Very naughty boy"
print a[:8].upper() + a[8:][::-1]
