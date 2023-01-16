areas = ["cuina", 7.88, "menjador", 13.0, "terrassa", 20.34, "lavabo", 6.55, "habitació1", 7.98, "habitació2", 12, "rebedor", 4.23]
#Imprimir el segon element
print(areas[1])

#Imprimir l'últim element
print(areas[-1])

#Imprimir l'àrea de la terrassa
print(areas[5])

#Imprimir del primer element al tercer
print(areas[:3])

#Imprimir del tercer element a l'últim
print(areas[2:])

#Imprimir el total de l'àrea de les dues habitacions
a = areas[9]
b = areas[11]
print(a+b)

#Modificar l'àrea del lavabo i imprimir la nova list area
areas[7] = 4.20
print(areas)

#Afegir l'àrea de “pati interior” i 2.78 a les últimes posicions.
#Imprimir la nova list area.
areas.extend(["pati interior", 2.78])
print(areas)