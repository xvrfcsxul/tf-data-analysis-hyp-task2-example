import pandas as pd
import numpy as np
import scipy.stats as stats

chat_id = 399364172

def solution(x: np.array, y: np.array) -> bool:
    correlation, p_value = stats.pearsonr(x, y)
    return p_value < 0.05
