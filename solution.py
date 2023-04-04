import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 12162367 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    #loc = x.mean()
        
    x = ((x * 2) / (50 * 50)
    alpha = 1 - p
    #np.quantile(-(expon.pdf(x) - 1/2), alpha / 2)
    #scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return np.quantile(-(expon.pdf(x) - 1/2), 1 - alpha / 2) / min(x), 
           np.quantile(-(expon.pdf(x) - 1/2), alpha / 2) / min(x)
