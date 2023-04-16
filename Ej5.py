import re


texto = input()

patron = "\\b(C/|Calle)\s([A-ZÑÁÉÍÓÚ][a-zñáéíóú]+)(,)?\s+(Nº?|nº?)?\s?([0-9]\d*),\s+(\d{5})\\b"
results = re.findall(patron, texto)

for match in results:
    print(match[5] + "-" + match[1] + "-" + match[4])





# yo vivo en la Calle Dulcinea N10, 28091 pero ella en la Calle Dulcinea 10, 28106 y mi primo en C/ Dulcinea Nº 10, 28936.
#28936-Dulcinea-10 28936-Dulcinea-10
#C/ Dulcinea, N10, 28936  Calle Dulcinea Nº10, 28936
#Calle Mester f n21, 90121, C/ Compañía n 1, 20919
# Calle Cleriñá  n21, 90121  Calle Cleriñá  n 21, 90121 Calle Cleriñá   21, 90121 Calle Cleriñá  N21, 90121 Calle Cleriñá  N 21, 90121
#C/ Ñeriñá  nº21, 90121, CalC/ Compañía n 1 20919le Ñeriñá  nº 21, 90121, Calle Ñeriñá  Nº21, 90121, Calle Ñeriñá  Nº 21, 90121