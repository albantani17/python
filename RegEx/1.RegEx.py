#RegEx module
import re

text = "Hujan di Pandeglang"
x = re.search("^Hujan.*Pandeglang$", text)  # ^ :

if x:
    print("Match found!")
else:
    print("No match found.")
