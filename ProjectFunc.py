import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from prophet import Prophet
import warnings
import numpy as np
import logging

warnings.filterwarnings("ignore", category=FutureWarning)
logging.getLogger("cmdstanpy").disabled = True


def get_data(company, period, data_type=None):
    print("Looking for data for", company, "for the period of", period)

    possible_periods = ['d', 'mo', 'y', 'ytd', 'max']
    for periods in possible_periods: 
        if not period.find(periods): 
            return f"Period not found. Periods can include: 'd', 'mo', 'y', 'ytd', 'max'."
        
    comp = yf.Ticker(company)
    data = comp.history(period)

    if data.empty:
        print("No Data Found")
        return 
    else:
        if data_type is not None:
            try:
                return data[data_type]
            except KeyError:
                return f"Invalid data_type(s): {data_type}. Choose from ['Open', 'High', 'Low', 'Close', 'Volume']"
        else:
            print("Data found, returning all data in the form of a DataFrame. WARNING: Do NOT train a model on this DataFrame, as it contains all data. Use a specific column like 'High', 'Low', etc.")
            return data

def train_prophet_model(data):
    if isinstance(data, pd.Series):
        df = data.reset_index()
        df['ds'] = df['Date'].dt.tz_localize(None) 
        df = df.rename(columns={data.name: 'y'})
        print(df)
        model = Prophet()
        model.fit(df)
        return model
    
    elif isinstance(data, pd.DataFrame):
        print("Choose a specific item to train the model on, like 'High', 'Low', etc. Put the choice in the get_data() method.")
        return 
    
def predict(model, steps):
    future = model.make_future_dataframe(periods=steps)
    forecast = model.predict(future)
    return forecast

def find_error(data, forecast):
    print("Calculating error metrics...")
    df_data = data.reset_index().rename(columns={'Date': 'ds', data.name: 'y'})
    df_data['ds'] = df_data['ds'].dt.tz_localize(None)  
    merged = pd.merge(df_data, forecast[['ds', 'yhat']], on='ds', how='left')
    merged['error'] = merged['y'] - merged['yhat']
    mse = (merged['error'] ** 2).mean()
    mae = merged['error'].abs().mean()
    return {"MSE": mse, "MAE": mae}

def bootstrap(data, n_iterations=1, steps=1): 
    predictions = []
    if data is None or data.empty:
        print("No data to bootstrap.")
        return predictions

    if not isinstance(data, pd.Series):
        raise TypeError("Expected data to be a pandas Series")

    for i in range(n_iterations):
        boot_sample = np.random.choice(data.values, size=len(data), replace=True)
        df = pd.DataFrame({
            "ds": data.index.tz_localize(None),
            "y": boot_sample
        })

        model = Prophet()
        model.fit(df)
        forecast = predict(model, steps)
        predictions.append(forecast[['ds', 'yhat']].tail(steps))

    return predictions[0]['yhat'].values

def to_list(data, steps, n_iter=1):
    temp_lists = [ [] for _ in range(steps) ]

    for _ in range(n_iter):
        preds = bootstrap(data, steps=steps)
        
        for i, val in enumerate(preds): 
            temp_lists[i].append(val)

    return temp_lists

def confidence_intervals(data, step=1, n_iter=1): 
    forecasts = to_list(data, step, n_iter)

    intervals = []

    for preds in forecasts: 
        lower = round(np.percentile(preds, 2.5), 2)
        upper = round(np.percentile(preds, 97.5), 2)
        intervals.append((lower, upper))

    return intervals




    




