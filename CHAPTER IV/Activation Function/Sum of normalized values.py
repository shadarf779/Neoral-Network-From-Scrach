layer_output = [4.8 ,1.21,2.385]
E = 2.71828182846
exp_values = []
for output in layer_output:
    exp_values.append(E**output)
norm_base = sum(exp_values)

norm_values = []

for value in exp_values:
    norm_values.append(value/norm_base)
print('Exponentiated values:',norm_base)
print('Normalized exponentiated values:',norm_values)

print('Sum of normalized values:', sum(norm_values))