def makeShampoo(word):
    if word == "cook":
        return "Shampoo"
    else:
        return word

phrase = "I asked you to cook the egg"
words = phrase.split(" ")
newWords = map(makeShampoo, words)
newPhrase = " ".join(newWords)

print "phrase:", phrase
print "words:", words
print "newWords:", newWords
print "newPhrase", newPhrase
