import re

def check_password(password):
    pattern = r'^(?=.*[a-z].*[a-z])(?=.*\d)(?=.*[^a-zA-Z0-9])(?!.*[,.!?])(?!.*[A-Z]).{8,}$'
    return bool(re.match(pattern, password))

print(check_password("rtG&3FG#Tr^e"))  
print(check_password("a^A1@*@1Aa"))  

print(check_password("пароль"))  
print(check_password("password"))  

