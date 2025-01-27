import os
# _____________________________________________________________
# Crea un Diccionario de key(listaStr) y value(IntroTeclado)
# from listTOdict_Tcld import listTOdict_byTcld as LTD

from classXindeX import XindeX 
from classTeclaData.listTOdict_Tcld import listTOdict_byTcld as TeclD
from classTeclaData.validator import ValidReg as VLID


def main():
    print(f'P R U E B A S   L I S T T O D I C T _ B Y T C L D\n{'='*50}')
 # 1- INSTANCIO EL OBJETO __________________________________________________________________________________
    The_X_Men = XindeX()
    # 2- CREO LOS MENUS Y SUS FUNCIONES ASOCIADAS _____________________________________________________________
    The_X_Men.addX(titulo='MenuPpal', 
                    lst_items=[ ("to_str" , to_string),("byDef" , None), ("byTcld" , byTcld)],
                    fraseHead="| - T A B L E R O - ")
    The_X_Men.addX(titulo='SUB_BYDEF', lst_items=[("sin Funciones",byDef), ("Con Funciones",byDef_2)])  
    The_X_Men.addX(titulo='SUB_BYTCLD', lst_items=[("uno",None), ("dos",None), ("tres", None)])


    # 3- COFIGURO LA GENETICA DEL INDICE___________________________________________________________________    
    The_X_Men.config(titulo='MenuPpal', suPadre=None , indexInPadre = None )
    The_X_Men.config(titulo='SUB_BYDEF', suPadre='MenuPpal', indexInPadre="byDef" )
    The_X_Men.config(titulo='SUB_BYTCLD', suPadre='MenuPpal', indexInPadre='byTcld' )

    # 4- LLAMO A MYSTYCA PARA VISUALIZAR EL MENU ____________________________________________________________
    retorno = The_X_Men.Mystyca(titulo='MenuPpal', configurado=True, execFunc=True, tipo_marcador='a', execAll=True, Loop=True , padX=50)
    # XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    print(f"::: T H E   E N D  en MAIN() ::: {retorno if retorno else 'no retorno'} ")

# ______________________________________________
# -Crea un Diccionario (K)strKey (V)strValue
#     -No permite '' (Nulo)
#     -No permite Configuracion
def to_string():    
    print(""" Genera un Diccionario a partir de un string de Key(str) y Value(str)
    >>> Ejemplo : 'toString() -> 'hola' -> Genera un diccionario 'hola' con los valores key y value introducidos. """)
    newDict = TeclD.toString(listaStrKeys=['toString()','(Key)str','(Value)str'])
    print(newDict)

# ________________________________
# Crea un Diccionario de key(listaStr) y value(IntroTeclado)
# Da el mismo resultado que toString (diccionario de str:str)
# --------------------------------
def byDef():
    print(f'{'~'*60}')
    print("""\n-Crea un Diccionario (K)strKey (V)[tipo,strValue] de str (sin lista de definicion de tipos (listaDef))
    -El Diccionario resultante es str si no le pones definicion de tipos.
    -Permite Nulo en la Entrada (permitenulo=True)
    -esCapital = False, no cambia las may de la listaKeys al imprimir\n""")
    twoDict=TeclD.byDef(listaStrKeys=['key 1','key 2','key 3','key 4'],                                   
                        permiteNulo=True,
                        esCapital=False)
    print(twoDict)

# ________________________________
# Crea un Diccionario de key(listaStr) y value(IntroTeclado) 
def byDef_2():
    print(f'{'~'*60}')
    print("""\n-Crea un Diccionario (K)strKey (V)[tipo,strValue] con Valores por Defecto
    -diccionario resultante es tipado  (con listaDef)  
    -Permite Nulo en la Entrada
    -esCapital=False, no cambia las may de la listaKeys al imprimir\n""")
    twoDict=TeclD.byDef(listaStrKeys=['byDef()','sin ListDef()','tipado Out', 'valores x Defecto'],                                   
                        listaDef= [(int,True),(float, False),(str, False)],
                        permiteNulo=True,
                        esCapital=False)
    print(twoDict)

def byTcld():
    # ________________________________
    # Crea un Diccionario de key(listaStr) y value(IntroTeclado)
    print(f'{'~'*60}')
    print("""\n-Crea un Diccionario (K)strKey (V)[tipo(strValue)]
    -diccionario resultante es Tipado al introducir el dato  (con listaDef)
    -Permite Nulo en la Entrada
    -esCapital=False, no cambia las may de la listaKeys al imprimir\n""")
    
    # boolean=bool('')        #Da Falso por defecto
    # boolean=bool(0)         #False
    # boolean=bool(1)         #True
    # boolean=bool(None)      #False

    oneDict=TeclD.byTcld( listaStrKeys=['byTcld()', 'ListaDef','Tipado Tcldo','permiteNulo'],
                        listaDef= [ (bool,True),(float, True),(bool, False),(int, False) ],
                        permiteNulo=True,
                        esCapital=False )
    print(oneDict)
    print(oneDict['ListaDef'])    
    
if __name__ == "__main__":
    os.system('cls')
    main()
