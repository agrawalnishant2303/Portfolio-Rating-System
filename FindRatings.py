#Calculate the rating for sharpe ratio.
def sharpeRatioRating(ratio):
    if ratio >= 2.5:
        return "AAA"
    elif ratio >= 2.0 and ratio < 2.5:
        return "AA"
    elif ratio >= 1.5 and ratio < 2:
        return "A"
    elif ratio >= 1.0 and ratio < 1.5:
        return "BBB"
    elif ratio >= 0.5 and ratio < 1.0:
        return "BB"
    elif ratio >= 0.0 and ratio < 0.5:
        return "B"
    elif ratio >= -0.5 and ratio < 0.0:
        return "C"
    elif ratio < -0.5:
        return "D"
#Calculate the rating for sortino ratio
def sortinoRatioRating(ratio):
    if ratio >= 3.0:
        return "AAA"
    elif ratio >= 2.5 and ratio < 3.0:
        return "AA"
    elif ratio >= 2.0 and ratio < 2.5:
        return "A"
    elif ratio >= 1.5 and ratio < 2.0:
        return "BBB"
    elif ratio >= 1.0 and ratio < 1.5:
        return "BB"
    elif ratio >= 0.5 and ratio < 1.0:
        return "B"
    elif ratio >= 0.0 and ratio < 0.5:
        return "C"
    elif ratio < 0.0:
        return "D"
#Calculate the rating for Maximum Drawdown
def maxDrawdownRating(ratio):
    if ratio < 0.1:
        return "AAA"
    elif ratio >= 0.1 and ratio < 0.15:
        return "AA"
    elif ratio >= 0.15 and ratio < 0.2:
        return "A"
    elif ratio >= 0.2 and ratio < 0.25:
        return "BBB"
    elif ratio >= 0.25 and ratio < 0.3:
        return "BB"
    elif ratio >= 0.3 and ratio < 0.35:
        return "B"
    elif ratio >= 0.35 and ratio < 0.4:
        return "C"
    elif ratio > 0.4:
        return "D"
#Calculate the rating for Calmar Ratio
def calmarRatioRating(ratio):
    if ratio >= 4.0:
        return "AAA"
    elif ratio >= 3.0 and ratio < 4.0:
        return "AA"
    elif ratio >= 2.0 and ratio < 3.0:
        return "A"
    elif ratio >= 1.5 and ratio < 2.0:
        return "BBB"
    elif ratio >= 1.0 and ratio < 1.5:
        return "BB"
    elif ratio >= 0.5 and ratio < 1.0:
        return "B"
    elif ratio >= 0.0 and ratio < 0.5:
        return "C"
    elif ratio < 0.0:
        return "D"
#Calculate the rating for Treynor Ratio
def treynorRatioRating(ratio):
    if ratio >= 0.5:
        return "AAA"
    elif ratio >= 0.4 and ratio < 0.5:
        return "AA"
    elif ratio >= 0.3 and ratio < 0.4:
        return "A"
    elif ratio >= 0.2 and ratio < 0.3:
        return "BBB"
    elif ratio >= 0.1 and ratio < 0.2:
        return "BB"
    elif ratio >= 0.0 and ratio < 0.1:
        return "B"
    elif ratio >= -0.1 and ratio < 0.0:
        return "C"
    elif ratio < -0.1:
        return "D"
#Calculate the rating for Information Ratio
def informationRatioRating(ratio):
    if ratio >= 1.0:
        return "AAA"
    elif ratio >= 0.8 and ratio < 1.0:
        return "AA"
    elif ratio >= 0.6 and ratio < 0.8:
        return "A"
    elif ratio >= 0.4 and ratio < 0.6:
        return "BBB"
    elif ratio >= 0.2 and ratio < 0.4:
        return "BB"
    elif ratio >= 0.0 and ratio < 0.2:
        return "B"
    elif ratio >= -0.2 and ratio < 0.0:
        return "C"
    elif ratio < -0.2:
        return "D"
#Calculate the rating for Alpha Annualized
def alphaAnnualizedRating(ratio):
    if ratio >= 0.05:
        return "AAA"
    elif ratio >= 0.03 and ratio < 0.05:
        return "AA"
    elif ratio >= 0.01 and ratio < 0.03:
        return "A"
    elif ratio >= 0.0 and ratio < 0.01:
        return "BBB"
    elif ratio >= -0.01 and ratio < 0.0:
        return "BB"
    elif ratio >= -0.03 and ratio < -0.01:
        return "B"
    elif ratio >= -0.05 and ratio < -0.03:
        return "C"
    elif ratio < -0.05:
        return "D"
#Calculate the rating for beta
def betaRating(ratio):
    if ratio >= 0.9 and ratio < 1.1:
        return "AAA"
    elif (ratio >= 0.8 and ratio < 0.9) or (ratio >= 1.1 and ratio < 1.2):
        return "AA"
    elif (ratio >= 0.7 and ratio < 0.8) or (ratio >= 1.2 and ratio < 1.3):
        return "A"
    elif (ratio >= 0.6 and ratio < 0.7) or (ratio >= 1.3 and ratio < 1.4):
        return "BBB"
    elif (ratio >= 0.5 and ratio < 0.6) or (ratio >= 1.4 and ratio < 1.5):
        return "BB"
    elif (ratio >= 0.4 and ratio < 0.5) or (ratio >= 1.5 and ratio < 1.6):
        return "B"
    elif (ratio >= 0.3 and ratio < 0.4) or (ratio >= 1.6 and ratio < 1.7):
        return "C"
    elif (ratio < 0.3) or (ratio > 1.7):
        return "D"
#Calculate the rating for omega ratio
def omegaRatioRating(ratio):
    if ratio >= 1.8:
        return "AAA"
    elif ratio >= 1.6 and ratio < 1.8:
        return "AA"
    elif ratio >= 1.4 and ratio < 1.6:
        return "A"
    elif ratio >= 1.2 and ratio < 1.4:
        return "BBB"
    elif ratio >= 1.1 and ratio < 1.2:
        return "BB"
    elif ratio >= 1.0 and ratio < 1.1:
        return "B"
    elif ratio >= 0.9 and ratio < 1.0:
        return "C"
    elif ratio < 0.9:
        return "D"
#Find the score based on the rating.
def calculateScoreForRating(rating):
    if rating == "AAA":
        return 8
    elif rating == "AA":
        return 7
    elif rating == "A":
        return 6
    elif rating == "BBB":
        return 5
    elif rating == "BB":
        return 4
    elif rating == "B":
        return 3
    elif rating == "C":
        return 2
    elif rating == "D":
        return 1