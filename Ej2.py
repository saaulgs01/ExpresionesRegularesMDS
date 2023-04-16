import re


texto = input()

patron = "\\bE?[-|\s]?\d{4}[-|\s]?[A-Z]{3}\\b"
results = re.findall(patron, texto)
for match in results:
    print(match)
#Mi tractor tiene la matricula E-1234 ABC, mi coche 0011AAB 1234ABC 1234 ABC 1234-ABC E1234ABC E-1234ABC E 1234ABC E-1234-ABC.
