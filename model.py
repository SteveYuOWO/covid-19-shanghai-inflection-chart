import numpy as np
from scipy.optimize import curve_fit

def curve_regression(df, interval):
    x = np.linspace(len(df), 1, len(df))
    y = df['无症状感染者']
    curve_func = lambda x, a, b, c: a * np.exp(-b * x) + c
    popt, pcov = curve_fit(curve_func, x, y)
    return curve_func(np.linspace(1, interval, interval), *popt)

