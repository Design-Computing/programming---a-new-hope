from colorama import Fore, Style


def add(a, b):
    return 4


def testAdding(aNumber, anotherNumber, theResult):
    testPhrase = "if I add {} and {} I expect {}"
    print testPhrase.format(aNumber, anotherNumber, theResult),
    if add(aNumber, anotherNumber) == theResult:
        print(Fore.GREEN + "AWWW yess!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "OHNOES!!" + Style.RESET_ALL)


testAdding(2, 2, 4)
testAdding(1, 3, 4)
testAdding(4, 0, 4)
testAdding(4, 4, 8)
testAdding('6', '9', 15)
