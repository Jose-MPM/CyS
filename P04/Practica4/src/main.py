# Open the input file for reading
with open('/Users/kary_agarcia/Documents/CyS/SecLists/Passwords/xato-net-10-million-passwords.txt', 'r') as input_file:

    # Open the output file for writing
    with open('/Users/kary_agarcia/Documents/CyS/out.txt', 'w') as output_file:

        # Loop over each line in the input file
        for line in input_file:

            # Split the line into individual words
            words = line.split()

            # Loop over each word in the line
            for word in words:

                # Check if the word has a length of 10
                if len(word) == 10:

                    # Count the number of digits in the word
                    num_digits = sum(1 for c in word if c.isdigit())

                    # Check if the word has at least 5 digits
                    if num_digits >= 5:

                        # Write the word to the output file
                        output_file.write(word + '\n')
