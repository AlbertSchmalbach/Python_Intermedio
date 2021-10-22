from list_and_dicts import clearConsole
from platform import python_implementation, python_version_tuple

clearConsole()

print(python_implementation())

for atr in python_version_tuple():
    print(atr)