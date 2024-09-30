import numpy as np

def calculate_delta_e(L1, a1, b1, L2, a2, b2):
    delta_e = np.sqrt((L2 - L1)**2 + (a2 - a1)**2 + (b2 - b1)**2)
    return delta_e

def analyze_data(merged_data):
    merged_data['Delta_E'] = calculate_delta_e(
        merged_data['L11'], merged_data['a11'], merged_data['b11'],
        merged_data['L'], merged_data['a'], merged_data['b']
    )
    return merged_data
