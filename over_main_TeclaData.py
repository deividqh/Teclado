import os
from classXindeX import XindeX 
from Sdata import Sdata
from datetime import date 
from datetime import time 

diccionario = {}

def sdata_int():
    global diccionario
    diccionario = Sdata.get_data( dicc=diccionario,key_dict='int', tipo = int,msg_entrada='INTRODUCE UN ENTERO', permite_nulo=True)    
    print(diccionario)
def sdata_float():
    global diccionario
    diccionario = Sdata.get_data( dicc=diccionario,key_dict='float', tipo = float,msg_entrada='INTRODUCE UN FLOAT', permite_nulo=True)    
    print(diccionario)
def sdata_str():
    global diccionario
    diccionario = Sdata.get_data( dicc=diccionario,key_dict='str',tipo=str,msg_entrada='INTRODUCE UN STRING', permite_nulo = True)
    print(diccionario)
def sdata_bool():
    global diccionario
    diccionario = Sdata.get_data( dicc=diccionario,key_dict='bool',tipo=bool,msg_entrada='QUIERES CONTINUAR( V / F )?', permite_nulo=True)    
    print(diccionario)
def sdata_dni():
    global diccionario
    diccionario = Sdata.get_data( dicc=diccionario,key_dict='dni',tipo='DNI',msg_entrada='INTRODUCE DNI (nnnnnnnnA)', permite_nulo=True)    
    print(diccionario)
def sdata_email():
    global diccionario
    diccionario = Sdata.get_data( dicc=diccionario,key_dict='email',tipo='EMAIL',msg_entrada='INTRODUCE email (a@a)', permite_nulo=True)    
    print(diccionario)
    print(diccionario)
def sdata_ip():
    global diccionario
    diccionario = Sdata.get_data( dicc=diccionario,key_dict='ip',tipo='IP',msg_entrada='INTRODUCE IP (127.0.0.1)', permite_nulo=True)    
    print(diccionario)
def sdata_date():
    global diccionario
    diccionario = Sdata.get_data( dicc=diccionario,key_dict='dat',tipo=date,msg_entrada='INTRODUCE FECHA (dd/mm/yyyy)', permite_nulo=True)    
    print(diccionario)
def sdata_time():
    global diccionario
    diccionario = Sdata.get_data( dicc=diccionario,key_dict='hor',tipo=time,msg_entrada='INTRODUCE HORA (HH:MM)', permite_nulo=True)    
    print(diccionario)
def sdata_list():
    global diccionario
    diccionario = Sdata.get_data( dicc=diccionario,key_dict='list',tipo=list,msg_entrada='LISTA SEPARANDO POR COMAS (1,2,3,...)', permite_nulo=True)
    print(diccionario)
def sdata_between():
    global diccionario
    diccionario = Sdata.get_data( dicc=diccionario,key_dict='between',tipo='between',msg_entrada=['VERTICAL', 'HORIZONTAL'], permite_nulo=True)    
    print(diccionario)

def sdata_reset():
    global diccionario
    Sdata.reset_valores_bydef()
    print(Sdata.VALORES_POR_DEFECTO)

def sdata_get():
    global diccionario
    valor_bydef = Sdata.get_valor_bydef(tipo=int)    
    print(valor_bydef)

def sdata_set():
    global diccionario
    valor_bydef = Sdata.set_valor_bydef(tipo=int, valor=17 )    
    print(Sdata.VALORES_POR_DEFECTO)

def info():
    print(""" 
    >>> CLASE ESTÁTICA ENTRA UNA KEY STR Y DEVUELVE UN DICCIONARIO CON VALUE LA ENTRADA X TECLADO 
    CON EL TIPO CORRECTO O VALOR POR DEFECTO O NULO (DEPENDIENDO DE LA CONFIGURACION).

    LOS TIPOS DE DATOS PUEDEN SER: str, int, float, bool, date, time, 'IP', 'DNI', 'EMAIL', 'BETWEEN', list, set, tuple.

    EL DICCIONARIO SE PUEDE IR AUTO-INCREMETANDO... INTRODUCIENDO DICC COMO PARAMETRO OPCIONAL DE UN DICCIONARIO QUE EXISTA.

    Ejemplo:
    
    >>> dict_result = Sdata.get_data( key_dict='l', tipo=list , msg_entrada='INTRODUCE LISTA SEPARANDO POR COMAS (1,2,3,...)', permite_nulo=True)
    >>> dict_result = Sdata.get_data( dicc=dict_result , key_dict='pos', tipo='between' , msg_entrada=['VERTICAL', 'HORIZONTAL'], permite_nulo=False)    
    >>> dict_result = Sdata.get_data( dicc=dict_result , key_dict='dat', tipo = date , msg_entrada='INTRODUCE FECHA (dd/mm/yyyy)')    
    >>> print(f'lista: {dict_result['l']} - fecha: {dict_result['dat']} - hora: {dict_result['pos']} ')


    TAMBIEN SE PUEDEN REASIGNAR LOS VALORES POR DEFECTO CON MYSCELANEA : 
    >>> get_valor_bydef(tipo) / set_valor_bydef(tipo, valor) / reset_valores_bydef()


    """)

def main():
    print(f'P R U E B A S   SDATA \n{'='*50}')
 # 1- INSTANCIO EL OBJETO __________________________________________________________________________________
    The_X_Men = XindeX()
    # 2- CREO LOS MENUS Y SUS FUNCIONES ASOCIADAS _____________________________________________________________
    The_X_Men.addX(titulo='MenuPpal', 
                    lst_items=[ ("TYPOS PYTHON",info),("FECHA/HORA",None),("ESPECIALS",None), ('ITERADORES', None), ('BETWEEN',sdata_between), ('MYSCELANEA', None)],
                    fraseHead="| - TECLADO -  ME PIDES TIPO Y YO TE LO DEVUELVO EN UN DICCIONARIO"
                    )
    The_X_Men.addX(titulo='SUB_TYPOS', lst_items=[("INT",sdata_int), ("FLOAT",sdata_float), ("STR",sdata_str), ("BOOL",sdata_bool)])  
    The_X_Men.addX(titulo='SUB_FECHA', lst_items=[("DATE",sdata_date), ("TIME",sdata_time)])
    The_X_Men.addX(titulo='SUB_ESPECIALS', lst_items=[("DNI",sdata_dni), ("MAIL",sdata_email), ("IP", sdata_ip)])
    The_X_Men.addX(titulo='SUB_ITERADORES', lst_items=[("LIST",sdata_list), ("TUPLE",sdata_list), ("SET", sdata_list)])
    The_X_Men.addX(titulo='SUB_MYSCELANEA', lst_items=[("RESET VALOR BY DEF",sdata_reset), ("GET VALOR BYDEF",sdata_get), ("SET VALOR BYDEF",sdata_set)])


    # 3- COFIGURO LA GENETICA DEL INDICE___________________________________________________________________    
    The_X_Men.config(titulo='MenuPpal', suPadre=None , indexInPadre = None )
    The_X_Men.config(titulo='SUB_TYPOS', suPadre='MenuPpal', indexInPadre="TYPOS PYTHON" )
    The_X_Men.config(titulo='SUB_FECHA', suPadre='MenuPpal', indexInPadre='FECHA/HORA' )
    The_X_Men.config(titulo='SUB_ESPECIALS', suPadre='MenuPpal', indexInPadre='ESPECIALS' )
    The_X_Men.config(titulo='SUB_ITERADORES', suPadre='MenuPpal', indexInPadre='ITERADORES' )
    The_X_Men.config(titulo='SUB_MYSCELANEA', suPadre='MenuPpal', indexInPadre='MYSCELANEA' )

    # 4- LLAMO A MYSTYCA PARA VISUALIZAR EL MENU ____________________________________________________________
    retorno = The_X_Men.Mystyca(titulo='MenuPpal', configurado=True, execFunc=True, tipo_marcador='a', execAll=True, Loop=True , padX=50)
    # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    print(f"::: T H E   E N D  en MAIN() ::: {retorno if retorno else 'no retorno'} ")

if __name__ == "__main__":
    os.system('cls')
    main()
