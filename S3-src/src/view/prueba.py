import os, sys

p = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(p)

from controller import user

usuario = user.User(email="sergio@gmail.com", password="12345")

try:
    logged_user = usuario.read_user()
    print(logged_user["email"])
except Exception as e:
    print(e)
