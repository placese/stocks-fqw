import pandas as pd
import numpy as np
from sklearn.multioutput import RegressorChain
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
import matplotlib.pyplot as plt


async def get_poly_predicts(regressor: list[tuple], predictor: list[tuple], degree: int) -> list[tuple]:
    """Returns prediction value"""
    print(len(regressor))
    print(len(predictor))
    x = [value[1] for value in regressor]
    y = [value[1] for value in predictor] 
    x = pd.DataFrame(x)
    y = pd.DataFrame(y)
    x_seq = np.linspace(x.min(), x.max(), 1).reshape(-1, 1)
    polyreg = make_pipeline(PolynomialFeatures(degree), LinearRegression())
    polyreg.fit(x, y)
    plt.figure()
    plt.scatter(x, y)
    prediction = polyreg.predict(x_seq)
    plt.plot(x_seq, prediction, color="black")
    plt.title("Polynomial regression with degree " + str(degree))
    plt.show()
    plt.savefig('poly.png')
    print(len(prediction))
    return prediction
    

async def get_linear_predicts(regressor: list[tuple], predictor: list[tuple], degree: int) -> list[tuple]:
    """Returns prediction value"""
    print(len(regressor))
    print(len(predictor))
    x = [value[1] for value in regressor]
    y = [value[1] for value in predictor] 
    x = pd.DataFrame(x)
    y = pd.DataFrame(y)
    x_seq = np.linspace(x.min(), x.max(), 300).reshape(-1, 1)
    model = LinearRegression()
    polyreg = make_pipeline(model)
    polyreg.fit(x, y)
    plt.figure()
    plt.scatter(x, y)
    prediction = polyreg.predict(x_seq)
    plt.plot(x_seq, prediction, color="black")
    plt.title("Linear regression")
    plt.show()
    plt.savefig('linear.png')
    print(len(prediction))
    return prediction


async def get_SMA(data: list[tuple], period: int) -> list[tuple]:
    """Returns simple mooving average"""
    result = []
    for index in range(len(data)-period+1):
        average_price = 0
        m = index
        trashhold = m + period
        for i in data[m:trashhold]:
            average_price += i[1]
        average_price /= period
        result.append((i[0], average_price))
    return result


# if __name__ == '__main__':
async def process_analysis():
    from app.api_requester.yahoo_finance_requester import get_ticker_from_api
    data_1 = await get_ticker_from_api('AMD')
    data_2 = await get_ticker_from_api('MSFT')
    res_1 = []
    res_2 = []
    for k in data_1.get("data"):
        res_1.append((k["time_stamp"], k["open"]))
    for k in data_2.get("data"):
        res_2.append((k["time_stamp"], k["open"]))
    
    # return await get_SMA(res_1, 5)

    return await get_poly_predicts(res_1, res_2, 1)
