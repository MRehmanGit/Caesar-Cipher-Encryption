def encryption(user_input, val):
    # Initialize the final encrypted string
    final_string = ""
    
    # Iterate through each character in the input string
    for letter in user_input:
        # Handle spaces
        if letter.isspace():
            final_string += " "
            continue
        
        # Handle non-alphabetical characters
        if not letter.isalpha():
            final_string += letter
            continue
        
        # Handle alphabetical characters
        if letter.isalpha():
            if letter.islower():  # Check if the letter is lowercase
                flag_it = True
                counter = 0
                inc_value = ord(letter)  # Get ASCII value of the letter
                
                while flag_it:
                    if counter != val:
                        if inc_value < 122:  # Check if within 'a' to 'z'
                            inc_value += 1
                            counter += 1
                        else:
                            # Reset to 'a' after 'z'
                            inc_value = ord('a')
                            counter += 1
                    else:
                        flag_it = False

                final_string += chr(inc_value)

            elif letter.isupper():  # Check if the letter is uppercase
                flag_it = True
                counter = 0
                inc_value = ord(letter)  # Get ASCII value of the letter
                
                while flag_it:
                    if counter != val:
                        if inc_value < 90:  # Check if within 'A' to 'Z'
                            inc_value += 1
                            counter += 1
                        else:
                            # Reset to 'A' after 'Z'
                            inc_value = ord('A')
                            counter += 1
                    else:
                        flag_it = False

                final_string += chr(inc_value)
            else:
                word = chr(ord(letter) + val)
                final_string += word

    return final_string

# Get user input for the string to be encrypted
user_char = input("Enter a character: ")
print("Regular string: ", user_char)

# Loop to get a valid shift value from the user
flag = True
while flag:
    value = int(input("Enter a shift value from 1 - 25 only: "))
    if 1 <= value <= 25:
        flag = False
    else:
        print("Invalid shift value. Please try again.")

# Print the encrypted string
print("Encrypted String: ", encryption(user_char, value))
