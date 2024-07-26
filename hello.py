import os

# Path to the counter file
counter_file = 'counter.txt'

# Initialize counter
if not os.path.exists(counter_file):
    with open(counter_file, 'w') as f:
        f.write('0')

# Read the current counter value
with open(counter_file, 'r') as f:
    counter = int(f.read())

# Increment the counter
counter += 1

# Write the new counter value back to the file
with open(counter_file, 'w') as f:
    f.write(str(counter))

# Append the message to the output file
output_file = 'output.txt'
with open(output_file, 'a') as f:
    f.write(f'hello world {counter}\n')
