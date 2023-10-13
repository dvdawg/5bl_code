import math

def create_weights(data):
    weights = [1 / math.sqrt(item) for item in data]
    return weights

# Initial data
t_squared = [1.81118, 2.68567, 4.52924, 6.26301, 8.1282, 9.34586]
moment_inertia = [63.0436, 88.3246, 138.8870, 189.4490, 240.0110, 290.5730]
simple_reg_slope = 30.5548

alpha_t_squared = [0.021657, 0.010935, 0.079338, 0.03866, 0.080031, 0.081111]
alpha_I = [0.160464, 0.186281, 0.326062, 0.499548, 0.681467, 0.866522]

# Calculating intermediaries
alpha_I_naught = [simple_reg_slope * alpha for alpha in alpha_t_squared]
new_alpha_I = [math.sqrt(alpha_i ** 2 + alpha_i_naught ** 2) for alpha_i, alpha_i_naught in zip(alpha_I, alpha_I_naught)]

weights = create_weights(new_alpha_I)

# Initialize slope
slope = 0.0

# Calculate linear reg slope
fraction_part = 0.0
denom = 0.0

for i in range(len(weights)):
    fraction_part += weights[i] * t_squared[i]

for i in range(len(weights)):
    for j in range(len(weights)):
        slope += (weights[j] * (weights[i] * moment_inertia[i] * t_squared[i]) - (weights[j] * t_squared[j]) * (weights[i] * moment_inertia[i]))

for i in range(len(weights)):
    denom += (weights[i] * (t_squared[i] ** 2))
sum_weights = 0.0
for i in range(len(weights)):
    sum_weights+=weights[i]
denom = sum_weights*denom

denom -= fraction_part ** 2
slope = slope / denom

# Calculate constant
c = 0.0
const_denom = 0.0

for i in range(len(weights)):
    c += (weights[i] * moment_inertia[i])
for i in range(len(weights)):
    c -= slope*(weights[i]*t_squared[i])
c = c / sum_weights
# Calculate alpha m
alpha_m = math.sqrt(sum_weights / denom)

# Calculate alpha c
alpha_c = 0.0
numerator = 0.0

for i in range(len(weights)):
    numerator += weights[i] * (t_squared[i] ** 2)

alpha_c = math.sqrt(numerator / denom)

# Calculate chi_squared
chi_squared = 0.0

for i in range(len(weights)):
    chi_squared += (weights[i] * (moment_inertia[i] - slope * t_squared[i] - c))**2

# Print results
print("Slope:", slope)
print("Constant:", c)
print("Alpha m:", alpha_m)
print("Alpha constant:", alpha_c)
print("Chi Squared:", chi_squared)
print(new_alpha_I)
