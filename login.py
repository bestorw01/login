allowedUsernames = ['mentor','rukky','bob']
allowedPassword = 'password'

print('lOGIN PAGE')

username = input('Enter username: ')


if username in allowedUsernames:
    password = input('Enter password: ')

    if password == allowedPassword:
        print(f'Welcome {username.capitalize()}')
    else:
        print('The password is incorrect')
else:
    print('The username you entered is not available')