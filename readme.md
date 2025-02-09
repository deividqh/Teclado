 
# CLASE ESTÁTICA ENTRA UNA KEY STR Y DEVUELVE UN DICCIONARIO CON VALUE LA ENTRADA X TECLADO 
# CON EL TIPO CORRECTO O VALOR POR DEFECTO O NULO (DEPENDIENDO DE LA CONFIGURACION).

-LOS TIPOS DE DATOS PUEDEN SER: str, int, float, bool, date, time, 'IP', 'DNI', 'EMAIL', 'BETWEEN', list, set, tuple.

-EL DICCIONARIO SE PUEDE IR AUTO-INCREMETANDO... INTRODUCIENDO DICC COMO PARAMETRO OPCIONAL DE UN DICCIONARIO QUE EXISTA.

Ejemplo:
* dict_result = Sdata.get_data( key_dict='l', tipo=list , msg_entrada='INTRODUCE LISTA SEPARANDO POR COMAS (1,2,3,...)', permite_nulo=True)
* dict_result = Sdata.get_data( dicc=dict_result , key_dict='pos', tipo='between' , msg_entrada=['VERTICAL', 'HORIZONTAL'], permite_nulo=False)    
* dict_result = Sdata.get_data( dicc=dict_result , key_dict='dat', tipo = date , msg_entrada='INTRODUCE FECHA (dd/mm/yyyy)')    
* print(f'lista: {dict_result['l']} - fecha: {dict_result['dat']} - hora: {dict_result['pos']} ')


# TAMBIEN SE PUEDEN REASIGNAR LOS VALORES POR DEFECTO CON MYSCELANEA : 
- get_valor_bydef(tipo) / set_valor_bydef(tipo, valor) / reset_valores_bydef()