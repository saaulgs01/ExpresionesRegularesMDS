import re


texto = input()

patron = r'(\b\d{4})-(\d{2})-(\d{2}\b)'
nuevo_formato = r'\3.\2.\1'
results = re.sub(patron, nuevo_formato, texto)


print(results)


#El  profesor  Isaac  Lozano  puso  una  fecha  de  entrega  el  a2023-04-16,  a  las  23:55
#El  profesor  Isaac  Lozano  puso  una  fecha  de  entrega  el  16.04.2023  a  las  23:55