# Make functions to use in app.py

# To hash passwords
import hashlib
# Check email
from email_validator import validate_email, EmailNotValidError
import re, os

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
UPLOAD_FOLDER = 'static/imgsClient'

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

def allowed_file(filename):
      return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

def duplicate(filename):
        path = os.path.join(UPLOAD_FOLDER,filename)
        # print(path)
        # print(os.path.isfile(path))
        if os.path.isfile(path):
            search = re.search(r'(\D*)(\d+)?(\.[^.]*)$', filename)
            file = search.groups() # get the full filename splitted
            i = 1
            # print(file)
            # print(os.path.join(UPLOAD_FOLDER,file[0]+str(i)+file[2]))
            while os.path.isfile(os.path.join(UPLOAD_FOLDER,file[0]+str(i)+file[2])):
                i += 1
            # print(t)
            filename = file[0]+str(i)+file[2]
        return filename

if __name__ == '__main__':
        test = 'hello'
        # print(hashPassword(test))
        verifyName('as')
        print(duplicate('barbero - copia.jpg'))