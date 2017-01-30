from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


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


def plotToCheck(activityList, gaps):
    c = Counter(activityList)
    counts = {}
    for a in activities:
        counts[a['name']] = c[a['name']]

    plt.bar(range(len(counts)), counts.values(), align='center')
    plt.xticks(range(len(counts)), counts.keys())

    plt.show()

    plt.hist(gaps)
    plt.show()


def gapTimes(minTime, maxTime, numberOfThings, method="bell"):
    if method == "bell":
        # https://docs.scipy.org/doc/numpy-1.10.0/reference/generated/numpy.random.normal.html
        gaps = np.random.normal(np.mean([minTime, maxTime]),  # mean
                                (maxTime - minTime) / 5,      # standard deviation
                                # 5 because most is captured by 3sd either side
                                # it's a horrible hack
                                numberOfThings)               # number of results
        return [abs(g) for g in gaps]  # catch very occasional -ve numbers
    elif method == "uniform":
        return np.random.uniform(minTime, maxTime, size=numberOfThings)
    elif method == "triangular":
        return np.random.triangular(minTime,
                                    np.mean([minTime, maxTime]),
                                    # TODO implement an adjustable mean
                                    maxTime,
                                    size=numberOfThings)


states = getStateNames(activities)
weights = getNormalisedScores(activities)
numberOfThings = 10
minTime = 1   # minutes
maxTime = 30  # minutes

activityList = np.random.choice(states, numberOfThings, p=weights)
# gap distribution options: "bell", "uniform", "triangular"
gaps = gapTimes(minTime, maxTime, numberOfThings, method="triangular")
schedule = zip(activityList, gaps)

# plotToCheck(activityList, gaps)

for t in schedule:
    print "Do a {} then work for {:.1f} minutes".format(t[0], t[1])


areas = [4.397498, 4.417111, 4.538467, 4.735034, 4.990129, 5.292455, 5.633938,
         6.008574, 6.41175, 5.888393, 2.861898, 2.347887, 2.459234, 2.494357,
         2.502986, 2.511614, 2.520243, 2.528872, 2.537501, 2.546129, 7.223747,
         7.223747, 2.448148, 1.978746, 1.750221, 1.659351, 1.669999]
divisons = [0.0, 0.037037, 0.074074, 0.111111, 0.148148, 0.185185, 0.222222,
            0.259259, 0.296296, 0.333333, 0.37037, 0.407407, 0.444444, 0.481481,
            0.518519, 0.555556, 0.592593, 0.62963, 0.666667, 0.703704, 0.740741,
            0.777778, 0.814815, 0.851852, 0.888889, 0.925926, 0.962963, 1.0]
weights = [a/sum(areas) for a in areas]
indexes = np.random.choice(range(len(areas)), 50000, p=weights)
samples = []
for i in indexes:
    samples.append(np.random.uniform(divisons[i], divisons[i+1]))

binwidth = 0.02
binSize = np.arange(min(samples), max(samples) + binwidth, binwidth)
plt.hist(samples, bins=binSize)
plt.xlim(xmax=1)
plt.show()
