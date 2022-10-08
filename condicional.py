# Ejercicio 10 condicional
print("")
tipo = int(input("""
********************************
Bella Napoli
Elija el tipo de pizza
\t1-para vegetariana        #con \t establezco una tabulacion
\t2-Para No vegetariano
 *******************************
"""))
if(tipo==1):
    eleccion = "Vegetariana"
    op=int(input("""
    Elija un ingrediente:
    1-Pimiento
    2-Tofu
    """))
    if op==1:
        ingrediente = "Pimiento"
    else:
        ingrediente = "Tofu"
else:
    eleccion = "No Vegetariana"
    op=int(input("""
    Elija un ingrediente:
    1-Peperoni
    2-Jamon
    3-Salmon
    """))
    if op==1:
        ingrediente = "Peperoni"
    elif op==2:
        ingrediente = "Jamon"
    else:
        ingrediente = "Salmon"

print(f"Usted eligio una pizza tipo {eleccion} los ingredientes son Tomate, Mozzarella y {ingrediente}")