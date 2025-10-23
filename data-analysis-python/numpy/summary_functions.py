import numpy as np

def calculate_mean(data):
    return np.mean(data)

def calculate_median(data):
    return np.median(data)

def calculate_variance(data):
    return np.var(data, ddof=1)

def calculate_std_dev(data):
    return np.std(data, ddof=1)

def calculate_min(data):
    return np.min(data)

def calculate_max(data):
    return np.max(data)

def calculate_percentiles(data, percentiles=[25, 50, 75]):
    return np.percentile(data, percentiles)
