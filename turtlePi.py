import turtle
import random
import math


def main():
    tina = turtle.Turtle()     # Make a new turtle, initialize values
    scribe = turtle.Turtle()
    tina.pensize(2)
    radius = 200
    tina.speed(5000)
    tina.tracer(2000)
    tina.penup()
    inCount = 0.0

    drawHelperCircle(radius)

    for i in range(10000):
        x = random.randrange(-200, 200)
        y = random.randrange(-200, 200)
        distanceFromHome = math.hypot(x, y)
        if distanceFromHome > radius:
            tina.color("red")
        else:
            tina.color("green")
            inCount += 1
        tina.goto(x, y)
        tina.dot(5)

        if i > 0:  # just checking that we don't try a divide by zero
            writeRatio(scribe, inCount, i)

    writeRatio(scribe, inCount, i)


def writeRatio(scribe, inCount, numTotalPoints):
    scribe.clear()
    scribe.penup()
    ratio = inCount*4/numTotalPoints
    scribe.write("{0:.5f}".format(ratio), False, "left", "30px Arial")


def drawHelperCircle(radius):
    t = turtle.Turtle()
    t.speed(5000)
    t.penup()
    t.goto(0, -radius)
    t.pendown()
    t.circle(radius, steps=100)


main()
