import os
import base64

some_set = set()

def generate():
    return base64.b32encode(os.urandom(3))[:5].decode('utf-8')

def generate_unique():
    string = generate()
    while string in some_set:
        string = generate()
    some_set.add(string)
    return string

for i in range(10):
      print(generate_unique())