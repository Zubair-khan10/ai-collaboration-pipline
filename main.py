import pandas as pd
from sklearn.linear_model import LogisticRegression

def load_data():
    print("data loading...")
    return pd.DataFrame()   # Correct DataFrame

def init_model():
    # initializing model
    model = LogisticRegression(max_iter=100)   # Student B ka change
    return model

def preprocess_data(df):
    print("handling missing values...")
    return df