import re

text = "Mi moto alpina derrapante"

new_text = re.sub("[aeiou]", "e", text)

print(new_text)