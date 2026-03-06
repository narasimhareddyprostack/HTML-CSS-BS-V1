import re

def validate_username(username):
    return bool(re.match(r'^(?=.*[A-Z])(?=.*[!@#$%^&*(),.?":{}|<>])(?=.*\d).{6}$', username))


print(validate_username("Pr@St9"))