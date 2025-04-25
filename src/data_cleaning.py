import pandas as pd


def clean(data):
    data = data.dropna()
    data.columns = [c.strip().lower() for c in data.columns]
    return data
