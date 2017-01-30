import random
from bisect import bisect


activities = [
              {"name": "air squat", "score": 1.0},
              {"name": "band passthrough", "score": 2.0},
              {"name": "handstand", "score": 3.0},
              {"name": "plank", "score": 4.0},
              {"name": "thorasic bridge", "score": 5.0},
              {"name": "touch toes", "score": 6.0},
             ]


def getNormalisedScores(activities):
    weights = [a["score"] for a in activities]
    normWeights = [(a)/sum(weights) for a in weights]
    return normWeights


def getStateNames(activities):
    return [a["name"] for a in activities]


def gapTimes(minTime, maxTime, numberOfThings, method="bell"):
    if method == "bell":
        return [abs(random.gauss((minTime + maxTime) * (maxTime - minTime) / 5))
                for x in range(numberOfThings)]
    elif method == "uniform":
        return [random.uniform(minTime, maxTime)
                for x in range(numberOfThings)]
    elif method == "triangular":
        return [random.triangular(minTime, maxTime, (minTime + maxTime) * 0.5)
                for x in range(numberOfThings)]


states = getStateNames(activities)
weights = getNormalisedScores(activities)
numberOfThings = 10
minTime = 1   # minutes
maxTime = 30  # minutes


def weighted_choice(values, weights):
    total = 0
    cum_weights = []
    for w in weights:
        total += w
        cum_weights.append(total)
    x = random.random() * total
    i = bisect(cum_weights, x)
    return values[i]


def np_random_choice_fake(states, size=None,  weights=None):
    # options = zip(states, weights)
    if size:
        return [weighted_choice(states, weights) for i in range(100)]
    return weighted_choice(states, weights)


activityList = np_random_choice_fake(states,
                                     size=numberOfThings,
                                     weights=weights)

# activityList = np.random.choice(states, numberOfThings, p=weights)
# gap distribution options: "bell", "uniform", "triangular"
gaps = gapTimes(minTime, maxTime, numberOfThings, method="triangular")
schedule = zip(activityList, gaps)

for t in schedule:
    print("Do a {} then work for {:.1f} minutes".format(t[0], t[1]))
