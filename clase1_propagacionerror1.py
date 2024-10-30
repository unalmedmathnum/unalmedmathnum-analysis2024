#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 11:54:08 2024

@author: manuela
"""

import pandas as pd

# Configuración para mostrar todas las columnas sin truncar
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)

# Funciones para calcular propagación de error en multiplicación y división
def propagation_error_multiplication(a, b, delta_a, delta_b):
    # Valores aproximados de a y b
    a_approx = a + delta_a
    b_approx = b + delta_b
    
    # Multiplicación exacta y aproximada
    exact_product = a * b
    approx_product = a_approx * b_approx
    
    cota_error_abs = abs(b*delta_a) + abs(a*delta_b)
    cota_error_rel = abs(delta_a/a) + abs(delta_b/b)
    
    # Cálculo del error absoluto y relativo
    abs_error = abs(exact_product - approx_product)
    rel_error = abs_error / abs(exact_product) #if exact_product != 0 else float('inf')
    
    return exact_product, approx_product, cota_error_abs, abs_error, cota_error_rel, rel_error

def propagation_error_division(a, b, delta_a, delta_b):
    # Valores aproximados de a y b
    a_approx = a + delta_a
    b_approx = b + delta_b
    
    # División exacta y aproximada
    exact_division = a / b #if b != 0 else float('inf')
    approx_division = a_approx / b_approx #if b_approx != 0 else float('inf')
    
    cota_error_abs = abs(delta_a/b) + abs(a*delta_b/(b**2))
    cota_error_rel = abs(delta_a/a) + abs(delta_b/b)
    
    # Cálculo del error absoluto y relativo
    abs_error = abs(exact_division - approx_division)
    rel_error = abs_error / abs(exact_division) #if exact_division != 0 else float('inf')
    return exact_division, approx_division, cota_error_abs, abs_error, cota_error_rel, rel_error

# Ejemplos de multiplicación y división
mul_example_1 = propagation_error_multiplication(1.0, -1.0, 0.1, 0.1)
mul_example_2 = propagation_error_multiplication(100.0, 50.0, -0.1, 0.2)

data = {
    "Operation": ["Mul", "Mul"],
    "Exact Result": [mul_example_1[0], mul_example_2[0]],
    "Approx. Result": [mul_example_1[1], mul_example_2[1]],
    "Max Abs.Error": [mul_example_1[2], mul_example_2[2]],
    "Absolute Error": [mul_example_1[3], mul_example_2[3]],
    "Max Rel.Error": [mul_example_1[4], mul_example_2[5]],
    "Relative Error": [mul_example_1[5], mul_example_2[5]]
}

df = pd.DataFrame(data)
#print(df)


# Ejemplos de division
div_example_1 = propagation_error_division(100.0, 100.0, 0.1, 0.1)
div_example_2 = propagation_error_division(1e5, 1e5 - 1.0, 1.0, -1.0)


data = {
    "Operation": ["Div", "Div"],
    "Exact Result": [div_example_1[0], div_example_2[0]],
    "Approx. Result": [div_example_1[1], div_example_2[1]],
    "Max Abs.Error": [div_example_1[2], div_example_2[2]],
    "Absolute Error": [div_example_1[3], div_example_2[3]],
    "Max Rel.Error": [div_example_1[4], div_example_2[4]],
    "Relative Error": [div_example_1[5], div_example_2[5]]
}

df = pd.DataFrame(data)
print(df)

# pd.set_option('display.precision', 16)
#print("{:.16f}".format(a))




