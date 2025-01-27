import os
# _____________________________________________________________
# Crea un Diccionario de key(listaStr) y value(IntroTeclado)
from listTOdict_Tcld import listTOdict_byTcld as LTD


def main():
    print(f'P R U E B A S   L I S T T O D I C T _ B Y T C L D\n{'='*50}')

    # ___________________________________
    print("""-Crea un Diccionario (K)strKey (V)strValue
    -No permite '' (Nulo)
    -No permite Configuracion
""")
    # newDict = LTD.toString(listaStrKeys=['toString()','(Key)str','(Value)str'])
    # print(newDict)
    # ________________________________
    # Crea un Diccionario de key(listaStr) y value(IntroTeclado)
    # Da el mismo resultado que toString (diccionario de str:str)
    # --------------------------------
    print(f'{'~'*60}')
    print("""\n-Crea un Diccionario (K)strKey (V)[tipo,strValue] de str (sin listaDef)
    -diccionario resultante es str  (sin listaDef)
    -Permite Nulo en la Entrada
    -esCapital=False, no cambia las may de la listaKeys al imprimir\n""")
    # twoDict=LTD.byDef(listaStrKeys=['byDef()','Sin ListDef','Tipado Out','PermiteNull en Teclado'],                                   
    #                     permiteNulo=True,
    #                     esCapital=False)
    # print(twoDict)

    # ________________________________
    # Crea un Diccionario de key(listaStr) y value(IntroTeclado) 
    print(f'{'~'*60}')
    print("""\n-Crea un Diccionario (K)strKey (V)[tipo,strValue] con Valores por Defecto
    -diccionario resultante es tipado  (con listaDef)  
    -Permite Nulo en la Entrada
    -esCapital=False, no cambia las may de la listaKeys al imprimir\n""")
    # twoDict=LTD.byDef(listaStrKeys=['byDef()','sin ListDef()','tipado Out', 'valores x Defecto'],                                   
    #                     listaDef= [(int,True),(float, False),(str, False)],
    #                     permiteNulo=True,
    #                     esCapital=False)
    # print(twoDict)
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

    oneDict=LTD.byTcld( 
                        listaStrKeys=['byTcld()', 'ListaDef','Tipado Tcldo','permiteNulo'],
                        listaDef= [ (bool,True),(float, True),(bool, False),(int, False) ],
                        permiteNulo=True,
                        esCapital=False
                    )
    print(oneDict)
    print(oneDict['ListaDef'])
    
    
if __name__ == "__main__":
    os.system('cls')
    main()