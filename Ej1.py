import re


texto = input()
pattern = "\\b\d{4}\\b"
results = re.findall(pattern, texto)
for match in results:
    print(match)
