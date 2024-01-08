import re

text = "70000000"

pattern = r"[\d{10}][^7|^8|^9]"

result = re.findall(pattern, text)

if result:
    print("Yes")
else:
    print("No")