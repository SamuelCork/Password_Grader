# Samuel Cork
# A self developed code to check inputs and decide whether they are strong or weak passwords.

# A function to check the length of the password.
def check_length(user_input):
    return len(user_input) >= 8 #checks if the password is greater than or equal to 8

# Check for uppercase and lowercase
def check_case(user_input):
    upper = any(char.isupper() for char in user_input)
    lower = any(char.islower() for char in user_input)
    return upper and lower

# Checks for numbers
def check_digit(user_input):
    return any(char.isdigit() for char in user_input)

# Checks for special Characters
def check_symbol(user_input):
    symbol = '!@#$%^&*()_+-=[]{}|,./<>?\\'
    return any(char in symbol for char in user_input)

#for looping future code
loop = True




# User prompt
print('Hello! Please input a password then press "Enter" to be graded.')


while loop:
    # user input
    password = input()
    if password == 'exit':
        loop = False
        break
    # Information on the users input
    print('Password length:', len(password))

    #Prompts for user readability
    print('Now grading your input.')

    #Gives output on the password and recommendations
    if check_length(password):
        print('Passed: Password contains at least 8 characters.')
    else: print('Failed: Make sure password is at least 8 characters.')
###
    if check_case(password):
        print('Passed: Password contains upper and lowercase letters.')
    else: print('Failed: Password must contain both upper and lowercase letters.')
###
    if check_digit(password):
        print('Passed: Password contains at least one digit.')
    else: print('Failed: Make sure password has at least one digit.')
###
    if check_symbol(password):
        print('Passed: (Optional) Password contains at least one symbol.')
    else: print('Optional: No symbol was entered, '
              'However NIST no longer recommends special characters.')

    print('')
    print('Try another password. or type "exit" to end the program.')
    print('')
###

