import random
import string
def fun():
    letters=string.ascii_lowercase+string.ascii_uppercase+string.digits+'!@#$%^&*()_+'
    length=random.randint(8,12)
    return ' '.join(random.choice(letters) for x in range(length))

print(fun())
