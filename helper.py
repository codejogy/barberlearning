# Make functions to use in app.py

# To hash passwords
import hashlib
# Check email
from email_validator import validate_email, EmailNotValidError
import re

def hashPassword(password):
        h = hashlib.blake2b(digest_size=20)
        h.update(password.encode('utf-8'))
        return h.hexdigest()

def verifyEmail(email):
        '''Check if the email is valid'''
        try:
            emailInfo = validate_email(email, check_deliverability=False)
        except EmailNotValidError:
            # If it's not valid, return ''
            return ''
        # Give back a normalized value to be used in the database
        return emailInfo.normalized
                
def verifyName(name):
    # 2 characters
    # not 100 characters
    if len(name) > 100:
          return ''
    if re.search(r'^[a-zA-Z \']+[a-zA-Z]$',name):
        return name
    else:
        return ''



if __name__ == '__main__':
        test = 'hello'
        print(hashPassword(test))
        verifyName('as')