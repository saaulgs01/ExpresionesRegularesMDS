import re


texto = input()

patronProfesor = "([a-z]+)\.([a-z]+)@urjc\.es"
resultsProfesor = re.findall(patronProfesor, texto)

patronAlumno = "([a-z])\.([a-z]{2,})\.(\d{4})@alumnos\.urjc\.es"
resultsAlumno = re.findall(patronAlumno, texto)



for match in resultsAlumno:
    print("alumno " + match[1] + " matriculado en " + match[2])

for match in resultsProfesor:
    print("profesor " + match[0] + " apellido " + match[1])




# escribir un email a \href{mailto:isaac.lozano@urjc.es}{isaac.lozano@urjc.es} \textbf{con copia a} \href{mailto:raul.martin@urjc.es}{raul.martin@urjc.es}
#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#alumno es {i.lozanoo.2015@alumnos.urjc.es, mientras que el del profesor es isaac.lozano@urjc.es"

#profesor isaac apellido lozano
#profesor isaac apellido lozano
#profesor raul apellido martin
#profesor raul apellido martin
