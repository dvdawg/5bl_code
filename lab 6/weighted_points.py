import math
import numpy

def create_weights(data):
    weights = [1/math.sqrt(data[0]), 1/math.sqrt(data[1]), 1/math.sqrt(data[2]), 1/math.sqrt(data[3]), 1/math.sqrt(data[4]), 1/math.sqrt(data[5])]
    return weights

#initial data
t_squared = [1.81118, 2.68567, 4.52924, 6.26301, 8.1282, 9.34586]
moment_inertia = [63.0436, 88.3246, 138.8870, 189.4490, 240.0110, 290.5730]
simple_reg_slope = 30.5548

alpha_t_squared = [0.021657, 0.010935, 0.079338, 0.03866, 0.080031, 0.081111]
alpha_I = [0.160464, 0.186281, 0.326062, 0.499548, 0.681467, 0.866522]

#calculating intermediaries
alpha_I_naught = [simple_reg_slope * alpha_t_squared[0], simple_reg_slope * alpha_t_squared[1], simple_reg_slope * alpha_t_squared[2], simple_reg_slope * alpha_t_squared[3], simple_reg_slope * alpha_t_squared[4], simple_reg_slope * alpha_t_squared[5]]
new_alpha_I = [math.sqrt((alpha_I[0])**2 + (alpha_I_naught[0])**2), math.sqrt((alpha_I[1])**2 + (alpha_I_naught[1])**2), math.sqrt((alpha_I[2])**2 + (alpha_I_naught[2])**2), math.sqrt((alpha_I[3])**2 + (alpha_I_naught[3])**2), math.sqrt((alpha_I[4])**2 + (alpha_I_naught[4])**2), math.sqrt((alpha_I[5])**2 + (alpha_I_naught[5])**2)]

weights = create_weights(new_alpha_I)

#calculate linear reg slope
slope = 0.0
fraction_part = 0.0
denom = 0.0
for i in weights:
    fraction_part = fraction_part + weights[i] * t_squared[i]
for i in weights: 
    for j in weights:
        slope += (weights[j]*(weights[i]*moment_inertia[i]*t_squared[i]) - (weights[j]*t_squared[j])*(weights[i]*moment_inertia[i]))
for i in weights:
    denom += (weights[j]*(weights[i]*(t_squared[i]**2)))
denom -= fraction_part**2
slope = slope / denom

#calculate constant
c = 0.0
const_denom = 0.0
for i in weights:
    c += (weights[i] * moment_inertia[i]) / weights[i]
for i in weights:
    const_denom += weights[i]
c -= (fraction_part * slope)/const_denom

#calculate alpha m
alpha_m = 0.0
alpha_m = math.sqrt(const_denom / denom)

#calculate alpha c
alpha_c = 0.0
numerator = 0.0
for i in weights:
    numerator += weights[i] * (t_squared[i])**2
alpha_c = math.sqrt(numerator / denom)

#calculate chi_squared
chi_squared = 0.0
for i in weights:
    chi_squared += weights[i] * (moment_inertia[i] - slope * t_squared[i] - c)

#print
print("Slope: " + slope)
print("constant: " + c)
print("Alpha m: " + alpha_m)
print("Alpha constant: " + alpha_c)
print("Chi Squared: " + chi_squared)

