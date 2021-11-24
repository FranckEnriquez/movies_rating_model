# import external libraries
import plotly.express as px


def scatter_multiple_plot(df, title):
    '''
    Scatter plot
    '''
    fig = px.scatter(df, x="threshold", y=[
                     "TN", "FP", "FN", "TP"], title=title)
    return fig.show()


def time_series_plot(df, x_col, y_col, title):
    '''
    Plot of a time series univariate
    '''
    fig = px.line(df, x=x_col, y=y_col, title=title)
    return fig.show()


def histogram_plot(df, rand_var, nbins, title, color):
    '''
    Plot a histogram distribution according its frequencies
    '''
    fig = px.histogram(df, x=rand_var, nbins=nbins, title=title, color=color)
    return fig.show()


def bar_plot(df, x_col, y_col, title):
    '''
    Bar plot of a variable
    '''
    fig = px.bar(df, x=x_col, y=y_col, title=title)
    return fig.show()
