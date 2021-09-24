import pandas as pd

# Set weights and bias
weight1 = 1.0
weight2 = 1.0
bias = -1.0

# Define inputs and outputs
map_inputs = [(1, 1), (1, 0), (0, 1), (0, 0)]
map_outputs = [True, True, True, False]
outputs = []

# Generate and check output
for input, output in zip(map_inputs, map_outputs):
    linear_combination = weight1 * input[0] + weight2 * input[1] + bias
    activation_output = int(linear_combination >= 0)
    if bool(activation_output) is output:
        is_correct_string = 'Yes'
    else:
        is_correct_string = 'No'
    outputs.append([input[0], input[1], linear_combination, activation_output, is_correct_string])
    
# Print output
dataframe = pd.DataFrame(outputs, columns = ['Input1', 'Input2', 'Linear Combination', 'Activation Output', 'Is Correct'])
print(dataframe.to_string(index=False))
