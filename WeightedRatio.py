#Calculate the composite score for all the ratios
def compositeScore(ratioWeights, ratioScoreBasedOnRatings):
    compScore = 0
    for key,value in ratioScoreBasedOnRatings.items():
        compScore = compScore + (value * ratioWeights[key])
    return compScore