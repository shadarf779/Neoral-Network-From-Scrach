import numpy as np

inputs =[4.8 , 1.21 , 2.385]

exp_values = np.exp(inputs)

print('exponentiated Values : ' , exp_values)

norm_values = exp_values /np.sum(exp_values)
print ('normalized exponentiated values:' , norm_values)
print ('sum of normalized values:', np.sum(norm_values))



