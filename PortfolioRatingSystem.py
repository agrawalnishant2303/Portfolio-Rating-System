#Import necessary functions
import yfinance as yf
import pandas as pd
import numpy as np
import datetime
import pyfolio as pf
import FindRatings as rate
import WeightedRatio as ratio
from dateutil.relativedelta import relativedelta

#Find the rating based on the score.
def calculateRatingForScore(score: float):
    if score >= 7.5 and score <= 8:
        return "AAA"
    elif score >= 7 and score < 7.5:
        return "AA"
    elif score >= 6 and score < 7:
        return "A"
    elif score >= 5 and score < 6:
        return "BBB"
    elif score >= 4 and score < 5:
        return "BB"
    elif score >= 3 and score < 4:
        return "B"
    elif score >= 2 and score < 3:
        return "C"
    elif score < 2:
        return "D"
def max_drawdown(prices):
    peak_value = prices.Close.max()
    trough_value = prices.Close.min()
    return (peak_value - trough_value)/peak_value
def information_ratio_calc(stockReturn, factorReturn):
    #IR is average return subtract by benchmark average return by deviation in its difference
    returnAfterSub = stockReturn.sub(factorReturn)
    stdDevOfDifference = returnAfterSub.std()
    return (stockReturn.mean() - factorReturn.mean()) / stdDevOfDifference
def treynor_ratio_calc(stockReturn, riskFreeReturn, beta):
    #Mean of adjusted return divided by beta
    adj_return = stockReturn - riskFreeReturn
    return (adj_return.mean() / beta) * 252 #There are around 252 trading days in an year
#Fetch the portfolio of any ticker by passing the ticker value, risk free return and factor return
def portfolioRatingSystem(checkStock, riskFreeReturn, factorStock, period):
    #Ticker for the required stock data
    ticker = yf.Ticker(checkStock)
    endDate = datetime.date.today()
    startDate = endDate - relativedelta(years = 10)
    stockData = ticker.history(start = startDate, end = endDate)
    stockData.index = stockData.index.tz_convert('utc')
    stockReturns = stockData.Close.pct_change()
    #Ticker for factor return stock
    factorTicker = yf.Ticker(factorStock)
    factorStockData = factorTicker.history(start = startDate, end = endDate)
    factorStockData.index = factorStockData.index.tz_convert('utc')
    factorStockReturns = factorStockData.Close.pct_change()
    #Fetching sharpe ratio
    sharpe_ratio = pf.timeseries.sharpe_ratio(stockReturns,risk_free=riskFreeReturn,period='daily')
    sharpe_ratio_rating = rate.sharpeRatioRating(sharpe_ratio)
    sharpe_ratio_score = rate.calculateScoreForRating(sharpe_ratio_rating)
    #Fetching sortino ratio
    sortino_ratio = pf.timeseries.sortino_ratio(stockReturns,required_return=riskFreeReturn,period='daily')
    sortino_ratio_rating = rate.sortinoRatioRating(sortino_ratio)
    sortino_ratio_score = rate.calculateScoreForRating(sortino_ratio_rating)
    #Fetching Calmar ratio
    calmar_ratio = pf.timeseries.calmar_ratio(stockReturns,period='daily')
    calmar_ratio_rating = rate.calmarRatioRating(calmar_ratio)
    calmar_ratio_score = rate.calculateScoreForRating(calmar_ratio_rating)
    #Fetching Maximum Drawdown
    max_drawdown_value = max_drawdown(stockData)
    max_drawdown_rating = rate.maxDrawdownRating(max_drawdown_value)
    max_drawdown_score = rate.calculateScoreForRating(max_drawdown_rating)
    #Fetching Beta
    beta = pf.timeseries.beta(stockReturns, factorStockReturns)
    beta_rating = rate.betaRating(beta)
    beta_score = rate.calculateScoreForRating(beta_rating)
    #Fetching Annualized Alpha
    alpha = pf.timeseries.alpha(stockReturns, factorStockReturns)
    alpha_rating = rate.alphaAnnualizedRating(alpha)
    alpha_score = rate.calculateScoreForRating(alpha_rating)
    #Fetching Information Ratio
    information_ratio = information_ratio_calc(stockReturns, factorStockReturns)
    information_ratio_rating = rate.informationRatioRating(information_ratio)
    information_ratio_score = rate.calculateScoreForRating(information_ratio_rating)
    #Fetching Omega Ratio
    omega_ratio = pf.timeseries.omega_ratio(stockReturns, riskFreeReturn)
    omega_ratio_rating = rate.omegaRatioRating(omega_ratio)
    omega_ratio_score = rate.calculateScoreForRating(omega_ratio_rating)
    #Fetching Treynor Ratio
    treynor_ratio = treynor_ratio_calc(stockReturns, riskFreeReturn, beta)
    treynor_ratio_rating = rate.treynorRatioRating(treynor_ratio)
    treynor_ratio_score = rate.calculateScoreForRating(treynor_ratio_rating)
    #Create a dict of constant weights considered and a dict of ratio score values
    weights = {"sharpe" : 0.2, "sortino" : 0.15, "maxDrawdown" : 0.1, "calmar" : 0.1, "treynor" : 0.1, "information" : 0.1, "alpha" : 0.1,
              "beta" : 0.1, "omega" : 0.05}
    ratio_score = {"sharpe" : sharpe_ratio_score, "sortino" : sortino_ratio_score, "maxDrawdown" : max_drawdown_score, "calmar" : calmar_ratio_score, "treynor" : treynor_ratio_score, "information" : information_ratio_score
                   , "alpha" : alpha_score, "beta" : beta_score, "omega" : omega_ratio_score}
    #Fetch the final combined score and rating of the portfolio
    combinedScore = ratio.compositeScore(weights, ratio_score)
    combinedRating = calculateRatingForScore(score = combinedScore)
    result = {"Stock" : checkStock,
              "Ratios" : [{"name" : "Sharpe Ratio", "value" : str(sharpe_ratio), "rating": sharpe_ratio_rating},
                         {"name" : "Sortino Ratio", "value" : str(sortino_ratio), "rating": sortino_ratio_rating},
                         {"name" : "Maximum Drawdown", "value" : str(max_drawdown_value), "rating": max_drawdown_rating},
                         {"name" : "Calmar Ratio", "value" : str(calmar_ratio), "rating": calmar_ratio_rating},
                         {"name" : "Treynor Ratio", "value" : str(treynor_ratio), "rating": treynor_ratio_rating},
                         {"name" : "Information Ratio", "value" : str(information_ratio), "rating": information_ratio_rating},
                         {"name" : "Alpha (Annualized)", "value" : str(alpha), "rating": alpha_rating},
                         {"name" : "Beta", "value" : str(beta), "rating": beta_rating},
                         {"name" : "Omega Ratio", "value" : str(omega_ratio), "rating": omega_ratio_rating}],
             "Combined Ratio": {"value" : str(combinedScore), "rating" : combinedRating}}
    return result