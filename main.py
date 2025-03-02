from fastapi import FastAPI
from enum import Enum
import PortfolioRatingSystem as prs
from fastapi.responses import JSONResponse
app = FastAPI()

class Period(str, Enum):
    DAILY: 'daily'
    WEEKLY: 'weekly'
    MONTHLY: 'monthly'
    ANNUALLY: 'annually'

def riskFreeReturnBasedOnPeriod(returns, period):
    if period == 'daily':
        return returns / 252
    elif period == 'weekly':
        return returns / 52
    elif period == 'monthly':
        return returns / 12
    elif period == 'annually':
        return returns

@app.get("/combinedRating/")
async def fetchCombinedRatingOfStock(checkStock:str , riskFreeReturn:float, factorStock:str, period:str = 'daily'):
   return JSONResponse(prs.portfolioRatingSystem(checkStock, riskFreeReturnBasedOnPeriod(riskFreeReturn, period), factorStock, period))