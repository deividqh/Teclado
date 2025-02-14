# Sdata 
## PIDE UN DATO AL USUARIO Y DEVUELVE UN DICCIONARIO ACUMULATIVO CON EL DATO CON EL TIPO Y FORMA CORRECTA: 
### CLASE ESTÁTICA,  
### DEVUELVE EL VALOR TIPADO AL TIPO Y FORMA. DA INFORMACION AL USUARIO DEL TIPO QUE TIENE QUE INTRODUCIR.
### TAMBIEN PUEDES DEFINIR SI ADMITES NULOS O NO ADMITES VALOR NULO.


- LOS TIPOS DE DATOS PUEDEN SER: str, int, float, bool, date, time, 'IP', 'DNI', 'EMAIL', 'BETWEEN', list, set, tuple.

- EL DICCIONARIO SE PUEDE IR AUTO-INCREMETANDO... INTRODUCIENDO DICC COMO PARAMETRO OPCIONAL DE UN DICCIONARIO QUE EXISTA.

- permite_nulo = False: Obliga a meter dato correcto
                 True:  Permite no meter Valor y se asigna el valor por defecto.

- msg_entrada = Frase(str) que se muestra para pedir el dato.
                list o str en caso de que tipo == between.

Ejemplo:
1. dat = Sdata.get_data( key_dict='L', tipo=list , msg_entrada='INTRO LIST  (1,2,3,...)', permite_nulo=True)
2. dat = Sdata.get_data( dicc=dat , key_dict='P', tipo='between' , msg_entrada=['VERTICAL', 'HORIZONTAL'], permite_nulo=False)    
3. dat = Sdata.get_data( dicc=dat , key_dict='F', tipo = date , msg_entrada='INTRODUCE FECHA (dd/mm/yyyy)')    

4. USAR = print(f'lista: {dat['L']} - fecha: {dat['F']} - hora: {dat['P']} ')


### TAMBIEN SE PUEDEN REASIGNAR LOS VALORES POR DEFECTO CON MYSCELANEA : 
1. get_valor_bydef(tipo) / set_valor_bydef(tipo, valor) / reset_valores_bydef()