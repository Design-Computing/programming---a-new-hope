import random
import math


def main():
    radius = 200
    inCount = 0.0

    for i in range(10000):
        x = random.randrange(-200, 200)
        y = random.randrange(-200, 200)
        distanceFromHome = math.hypot(x, y)
        if distanceFromHome < radius:
            inCount += 1

        if i > 0:  # just checking that we don't try a divide by zero
            writeRatio(inCount, i)

    writeRatio(inCount, i)


def writeRatio(inCount, numTotalPoints):
    ratio = inCount*4/numTotalPoints
    print "{0:.5f}".format(ratio)


main()
