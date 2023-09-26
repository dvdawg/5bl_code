import math


err_t = 0.003317
err_l = 0
val_t = 1.122
val_l = 0.4833

experimental_err = 0.01
# error calc

del_t = (-8 * ((math.pi) ** 2) * val_l) / ((val_t) ** 3)
del_l = (4 * (math.pi) ** 2) / ((val_t) ** 2)

alpha_g = math.sqrt((del_t * err_t) ** 2 + (del_l * err_l) ** 2)

# agreement test
alpha_g = 0.06527
tot_err = math.sqrt((experimental_err) ** 2 + alpha_g ** 2)

print (tot_err)