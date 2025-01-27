T e c l a d o  es una clase que convierte los datos de entrada por teclado en diccionarios según la configuración de la clase.
Tiene varias clases dentro del archivo:
[ byDef ]
# Funcion Que hace Tipado del diccionario una vez introducidos todos los datos.
  # En caso de que no se ajusten a los datos de tipo mete los valores por defecto. 
  # Lo mas importate es que el analisis se hace Después de introducir los datos.
# Sobre re.sub: 
  # re.sub (pattern, repl, string, count=0, flags=0)
  #  repl    => Cadena de texto o función con el valor que reemplazará las coincidencias del patrón en la cadena.
  #  string  => La cadena en la que se realizará la búsqueda y el reemplazo
  #  count (opcional) => Número máximo de reemplazos a realizar. Si se establece en 0, reemplazará todas las coincidencias
  #  flags (opcional) => Modificadores de la expresión regular, como re.IGNORECASE para hacer la búsqueda sin diferenciar             entre mayúsculas y minúsculas.
# >>> Ejemplo => 
# dictRetorno = {
# strKey : re.sub(patron, 
#             lambda match: listTOdict_byTcld.__introByDef(match, options), 
#             strKey) 
#             for strKey in listaStrKeys
    # ***************************************************
 
[ byTcld ]

# *******************************************
    # Igual que byDef() pero obliga (permiteNulo=True) a introducir el dato buenoo DESDE EL TECLADO
    # Funcion Que hace Tipado del diccionario JUSTO DESPUÉS DE INTRODUCIR LOS DATOS.
        # OBLIGA A INTRODUCIR EL DATO CORRECTO.
        # En caso de que no se ajusten a los datos de tipo mete los valores por defecto. 
        # Lo mas importate es que el analisis se hace en el momento de Introducir los datos.
    # *******************************************
