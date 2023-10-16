import paq

# Initialize variables
c = X1 = X2 = X3 = X4 = X5 = b = a = X6 = X7 = X8 = X9 = X10 = 0

# Define a function to count 255 and 0 bits
def count_bits(x):
    c = x.count
    return c(b'\xff') + c(b'\x00')

# Define a function to count X2 repetitions
def count_x2_repeats(x):
    return x.count(b'\xff\xff') + x.count(b'\x00')

# Prompt the user for the number of repetitions (number of times to repeat the circle)
num_repetitions_outer = 1000  # Repeat the circle 1000 times

for _ in range(num_repetitions_outer):
    # Reset variables X1 to X10 at the beginning of each repetition
    X1 = X2 = X3 = X4 = X5 = b = a = X6 = X7 = X8 = X9 = X10 = 0

    # Prompt the user for the number of repetitions within each outer repetition
    num_repetitions_inner = int(input("Enter the number of inner repetitions: "))

    # Loop based on the number of inner repetitions
    for _ in range(num_repetitions_inner):
        # Get file names for input and output
        input_file_name = input("Enter the name of the input file: ")
        output_file_name = input("Enter the name of the output file: ")

        try:
            # Attempt to open the input file
            with open(input_file_name, 'rb') as file:
                data = file.read()

            # Prompt the user to choose between compression and extraction
            user_option = input("Choose an option: (1) Compress (2) Extract: ")

            if user_option == '1':
                # Perform compression
                compressed_data = paq.compress(data)
            elif user_option == '2':
                # Perform extraction
                compressed_data = paq.decompress(data)
            else:
                print("Invalid option. Please choose (1) Compress or (2) Extract.")
                continue

            # Write the result to the output file
            with open(output_file_name, 'wb') as file:
                file.write(compressed_data)

            # Count 255 and 0 bits added
            a = count_bits(compressed_data)
            b += a

            # Count repetitions of X2
            X5 += count_x2_repeats(compressed_data)

            # Update counters and flags
            X3 += 1
            X4 += 1

            # Extend X6 to X10 as needed
            X6 += a  # Count of 255 bits added
            X7 += b  # Count of 0 bits added
            X8 += X1  # Extend X8 as needed
            X9 += X2  # Extend X9 as needed
            X10 += X3  # Extend X10 as needed

            print(f'File {input_file_name} has been {"compressed" if user_option == "1" else "extracted"} and saved as {output_file_name}')

        except FileNotFoundError:
            print(f"File {input_file_name} not found. Please make sure the file exists.")

# Write results to a file
with open('x_values.txt', 'w') as file:
    file.write(f'X1={X1}\nX2={X2}\nX3={X3}\nX4={X4}\nX5={X5}\nX6={X6}\nX7={X7}\nX8={X8}\nX9={X9}\nX10={X10}')

# Print the final results
print(f'Repeats of X1 at 1-255: {X2}')
print(f'Repeats of X3: {X3}')
print(f'Repeats of X2 repeats 0 or 65535-255-1: {X5}')
print(f'Count of 255 bits added: {X6}')
print(f'Count of 0 bits added: {X7}')