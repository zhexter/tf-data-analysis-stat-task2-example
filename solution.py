import pandas as pd
import numpy as np

from scipy.stats import norm, expon


chat_id = 12162367 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    n = len(x)
    left = (-min(-x) - 1 / 2) / (50**2 / 2)
    right = (-np.log(alpha) / n -min(-x) - 1 / 2) / (50**2 / 2)
    return left, right
