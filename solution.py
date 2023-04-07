import pandas as pd
import numpy as np


chat_id = 751331790 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    t=10
    n = len(x)
    mu = -37
    sigma = np.exp(1) 
    error = np.random.normal(mu, sigma, n) # ошибки
    a = error/t 
    # x - скорость
    
    return a.mean() # Ваш ответ  
