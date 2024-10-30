#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 10:31:49 2024

@author: manuela
"""

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# Código en Python que muestra la propagación del error en suma y resta.
# Se calculan tanto el error absoluto como el error relativo en cada caso.

def propagation_error_sum(a, b, delta_a, delta_b):
    # Valores aproximados de a y b
    a_approx = a + delta_a
    b_approx = b + delta_b
    
    sum_deltas = abs(delta_a) + abs(delta_b)
    
    # Suma exacta y suma aproximada
    exact_sum = a + b
    approx_sum = a_approx + b_approx
    
    # Cálculo del error absoluto y relativo
    abs_error = abs(exact_sum - approx_sum)
    rel_error = abs_error / abs(exact_sum) #if exact_sum != 0 else float('inf')
    
    return exact_sum, approx_sum, sum_deltas, abs_error, rel_error

def propagation_error_subtraction(a, b, delta_a, delta_b):
    # Valores aproximados de a y b
    a_approx = a + delta_a
    b_approx = b + delta_b
    
    sum_deltas = abs(delta_a) + abs(delta_b)
    
    # Resta exacta y resta aproximada
    exact_diff = a - b
    approx_diff = a_approx - b_approx
    
    # Cálculo del error absoluto y relativo
    abs_error = abs(exact_diff - approx_diff)
    rel_error = abs_error / abs(exact_diff) #if exact_diff != 0 else abs_error / 1E-16
    
    return exact_diff, approx_diff, sum_deltas, abs_error, rel_error

# Ejemplos de suma
sum_example_1 = propagation_error_sum(1.0, 1.0, 0.1, -0.2)
sum_example_2 = propagation_error_sum(100.0, 50.0, -0.1, 0.2)

data = {
    "Operation": ["Sum", "Sum"],
    "Exact Result": [sum_example_1[0], sum_example_2[0]],
    "Approx. Result": [sum_example_1[1], sum_example_2[1]],
    "Sum Errors": [sum_example_1[2], sum_example_2[2]],
    "Absolute Error": [sum_example_1[3], sum_example_2[3]],
    "Relative Error": [sum_example_1[4], sum_example_2[4]]
}

df = pd.DataFrame(data)
print(df)


# Ejemplos de resta
sub_example_1 = propagation_error_subtraction(100.0, 100.0, -0.1, 0.1)
sub_example_2 = propagation_error_subtraction(1e5, 1e5 - 1.0, 1.0, -1.0)


data = {
    "Operation": ["Sub", "Sub"],
    "Exact Result": [sub_example_1[0], sub_example_2[0]],
    "Approx. Result": [sub_example_1[1], sub_example_2[1]],
    "Sum Errors": [sub_example_1[2], sub_example_2[2]],
    "Absolute Error": [sub_example_1[3], sub_example_2[3]],
    "Relative Error": [sub_example_1[4], sub_example_2[4]]
}

df = pd.DataFrame(data)
#print(df)




