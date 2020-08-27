user_name =input('What is your username?\n')
password = input('Enter your password:')
length_password = len(password)
hidden_password= '*'*length_password
print(f'{user_name}, your password {hidden_password} is {length_password} letters long')