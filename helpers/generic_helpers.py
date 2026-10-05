

import random
import string

def generate_random_email_and_password(domain=None, prefix=None):

    if not domain:
        domain = "email.com"
    if not prefix:
        prefix = "testuser"

    rand_string = "".join(random.choices(string.ascii_lowercase, k=10))
    rand_email = prefix + "_" + rand_string + "@" + domain

    rand_password = "".join(random.choices(string.ascii_letters, k=10))

    rand_info = {
        "email" : rand_email,
        "password" : rand_password
    }

    return rand_info