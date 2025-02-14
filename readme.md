# Sdata 
## PIDE UN DATO AL USUARIO Y DEVUELVE UN DICCIONARIO: 
### CLASE ESTÁTICA,  
### BACK EL VALOR CON EL TIPO CORRECTO O VALOR POR DEFECTO O NULO (DEPENDIENDO DE LA CONFIGURACION).

> LOS TIPOS DE DATOS PUEDEN SER: str, int, float, bool, date, time, 'IP', 'DNI', 'EMAIL', 'BETWEEN', list, set, tuple.

> EL DICCIONARIO SE PUEDE IR AUTO-INCREMETANDO... INTRODUCIENDO DICC COMO PARAMETRO OPCIONAL DE UN DICCIONARIO QUE EXISTA.

> permite_nulo = False: Obliga a meter dato correcto, True: Valor Nulo.

> msg_entrada = Frase(str) que se muestra para pedir el dato.
                list o str en caso de que tipo == between.

Ejemplo:
1. dict_result = Sdata.get_data( key_dict='l', tipo=list , msg_entrada='INTRODUCE LISTA SEPARANDO POR COMAS (1,2,3,...)', permite_nulo=True)
2. dict_result = Sdata.get_data( dicc=dict_result , key_dict='pos', tipo='between' , msg_entrada=['VERTICAL', 'HORIZONTAL'], permite_nulo=False)    
3. dict_result = Sdata.get_data( dicc=dict_result , key_dict='dat', tipo = date , msg_entrada='INTRODUCE FECHA (dd/mm/yyyy)')    
4. print(f'lista: {dict_result['l']} - fecha: {dict_result['dat']} - hora: {dict_result['pos']} ')


### TAMBIEN SE PUEDEN REASIGNAR LOS VALORES POR DEFECTO CON MYSCELANEA : 
1. get_valor_bydef(tipo) / set_valor_bydef(tipo, valor) / reset_valores_bydef()