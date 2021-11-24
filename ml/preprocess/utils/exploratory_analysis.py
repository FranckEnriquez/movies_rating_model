# import external libraries
import pandas as pd
import numpy as np

def generate_quality_report(df):
    '''
    This functions creates a dataframe with the main
    and basic information of the input
    '''
    #  features
    columns = pd.DataFrame(list(df.columns.values),
                           columns=['names'],
                           index=list(df.columns.values))

    #  types of data
    data_types = pd.DataFrame(df.dtypes, columns=[
                              'data_types'])  # Nombre de la columna

    #  missing values
    missing_values = pd.DataFrame(df.isnull().sum(), columns=[
                                  'missing_values'])  # No hay datos perdidos
    
    #  present_values
    present_values = pd.DataFrame(df.count(), columns=['present_Values'])
    
    #  unique values
    unique_values = pd.DataFrame(columns=['unique_values'])
    for col in list(df.columns.values):
        unique_values.loc[col] = [df[col].nunique()]

    #  min values
    min_values = pd.DataFrame(columns=['Min'])
    for col in list(df.columns.values):
        try:
            min_values.loc[col] = [df[
                col].min()] 
        except:
            pass

    #   max values
    max_values = pd.DataFrame(columns=['Max'])
    for col in list(df.columns.values):
        try:
            max_values.loc[col] = [df[
                col].max()]
        except:
            pass

    # data_quality_report
    data_quality_report = columns.join(data_types).join(missing_values).join(present_values).join(unique_values).join(
        min_values).join(max_values)
    return data_quality_report

def number_of_bins(n):
    '''
    Return the number of bins according the Sturges rule
    '''
    K = int(round(1 + 3.322 * np.log(n)))
    return K