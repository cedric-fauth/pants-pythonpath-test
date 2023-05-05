import os

print(os.getenv("hello"))
print(os.getenv("PYTHONPATH"))

print("Now we call the lib")

# just an example the lib could be anywhere on the system but can only be imported if PYTHONPATH is set correctly
import lib

