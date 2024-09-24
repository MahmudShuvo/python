import random
import string

pass_len=12
charvalues= string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

password = ""
for i in range(pass_len):
    password += random.choice(charvalues)

print("your random password is:", password)

# val=random.choice(['s','h','u','v','o'])