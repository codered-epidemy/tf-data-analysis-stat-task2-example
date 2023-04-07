import pandas as pd
import numpy as np
import math

from scipy.stats import norm


chat_id = 191207196 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = p
    s = sum(x)/len(x)
    se = sigma/math.sqrt(len(x))
    low_bound, up_bound = st.norm.interval(alpha, loc=s, scale=se)
    return low_bound, up_bound
