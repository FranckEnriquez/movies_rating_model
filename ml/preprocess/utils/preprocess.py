# import external libraries
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency


def cramers_v(x, y):
    '''
    Cramer's V helps to find the "correlation" between
    categorical varibles
    '''
    confusion_matrix = pd.crosstab(x, y)
    chi2 = chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2/n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2-((k-1)*(r-1))/(n-1))
    rcorr = r-((r-1)**2)/(n-1)
    kcorr = k-((k-1)**2)/(n-1)
    return np.sqrt(phi2corr/min((kcorr-1), (rcorr-1)))


def preprocess(df, drop_col1, drop_col2):
    def feature_engineering(df):
        '''
        All type of feature engineering
        '''
        # Change the data type: from object to datetime
        df['timestamp'] = pd.to_datetime(
            df['timestamp'], infer_datetime_format=True)

        # Time features
        df['weekday'] = df['timestamp'].dt.dayofweek
        df['month'] = df['timestamp'].dt.month
        df['year'] = df['timestamp'].dt.year

        # get dummies forom time features
        weekday_dummy = pd.get_dummies(
            df['weekday'], prefix='weekday', prefix_sep='_')
        month_dummy = pd.get_dummies(
            df['month'], prefix='month', prefix_sep='_')
        year_dummy = pd.get_dummies(
            df['month'], prefix='month', prefix_sep='_')

        # Join dummies & dataset
        df = pd.concat([df, weekday_dummy, month_dummy, year_dummy], axis=1)
        return df

    df = feature_engineering(df)

    def label_feature(df):
        '''
        Creation of a label feature
        '''
        df['label'] = np.where(df['rating'] >= 4.0, 1, 0)
        return df

    df = label_feature(df)

    def drop_columns(df, drop_col1, drop_col2):
        '''
        Eliminates all the not necessary or duplicate
        columns
        '''
        df = df.drop(drop_col1, axis=1)
        df = df.drop(drop_col2, axis=1)
        return df

    df = drop_columns(df, drop_col1, drop_col2)
    return df
