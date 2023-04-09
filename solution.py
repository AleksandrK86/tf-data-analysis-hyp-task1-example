import pandas as pd
import numpy as np
import math
from scipy import stats

chat_id = 1105105523 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  
    alpha=0.02
    
    p_value=proportions_ztest([x_success, y_success], [x_cnt, y_cnt])[1]
    
    print(p_value)
    
    if (p_value < alpha):
      return True
    else: 
      return False
