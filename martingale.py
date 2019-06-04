# Empirically Test the Martingale betting system.
# Runs many rounds of a single-zero roulette game and prints statistics.
# The constants at the top of the file are the parameters to the system.

import math
import random

STARTING_CASH = 46000.0
EXIT_CASH = 70000.0
MIN_BET = 2000
NUM_ROUNDS = 100000
ODDS = .486

metCriteriaCount = 0
highestCashSum = 0
trialsLengthSum = 0

print("Running...")

for i in range(NUM_ROUNDS):
    cash = STARTING_CASH
    numLosses = 0
    highestCash = cash
    metExitCriteria = False
    j = 0
    while cash >= MIN_BET:
        # print((j, cash, numLosses))
        didWin = True if random.uniform(0, 1) <= ODDS else False
        amount = min(cash, MIN_BET * math.pow(2, numLosses))
        amount = amount if didWin else -amount
        numLosses = 0 if didWin else numLosses + 1
        cash += amount
        j += 1
        if highestCash < cash:
            highestCash = cash
        if not metExitCriteria and cash >= EXIT_CASH:
            metExitCriteria = True
            trialsLengthSum += j

    metCriteriaCount += 1 if metExitCriteria else 0
    highestCashSum += highestCash

metCriteriaRatio = metCriteriaCount / NUM_ROUNDS
averageTrialsLength = 0 if metCriteriaRatio <= 0 else (trialsLengthSum / NUM_ROUNDS) * (1 / metCriteriaRatio)

print("Did meet exit criteria: " + str(metCriteriaRatio))
print("Average successful trial length: " + str(averageTrialsLength))
print("Highest cash average: " + str(highestCashSum / NUM_ROUNDS))
