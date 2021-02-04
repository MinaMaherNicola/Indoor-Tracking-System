import math


def calculateDistance(ssids, current):
    distance = []
    for i in range(len(ssids)):
        if (current[0] == ssids[i][0]):
            distance.append(abs(current[1] - ssids[i][1]))

        elif (current[1] == ssids[i][1]):
            distance.append(abs(current[0] - ssids[i][0]))

        else:
            distance.append(round(math.sqrt(
                ((current[0] - ssids[i][0]) ** 2) + ((current[1] - ssids[i][1]) ** 2)), 3))

    return distance
