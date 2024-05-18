class AhorcadoView:
    #Constructor
    def __init__(self):
        self.__cadena = []
    
    #Insertar por parametro la palabra del AhorcadoModel.py
    def preparar_juego_visual(self,palabra):
        print(f"{palabra} - {len(palabra)}")
        for i in range(len(palabra)):
            self.__cadena.append("_")
    
    def actualizar_cadena(self,palabra_buscada,letra):
        index = 0
        while index < len(palabra_buscada):
            index = palabra_buscada.find(letra,index)
            if index == -1:
                break
            self.__cadena[index]=letra
            index+=1
        # self.__cadena[list(palabra_buscada).index(letra)] = letra
    
    def dibujar_ahorcado(self,vidas,palabra_buscada):
        if vidas==6:
            print("================")
            print(" +----+")
            print(" |    |")
            print("      |")
            print("      |")
            print("      |")
            print(self.__cadena)
            str = f"================\n+----+\n |    |\n      |\n      |\n      |\n {self.__cadena}"
            return str

        elif vidas==5:
            print("================")
            print(" +----+")
            print(" |    |")
            print(" o    |")
            print("      |")
            print("      |")
            print(self.__cadena)
            str = f"================\n+----+\n |    |\n o    |\n |    |\n      |\n {self.__cadena}"
            return str

        elif vidas==4:
            print("================")
            print(" +----+")
            print(" |    |")
            print(" o    |")
            print(" |    |")
            print("      |")
            print(self.__cadena)
            str = f"================\n+----+\n |    |\n o    |\n |    |\n      |\n {self.__cadena}"
            return str

        elif vidas==3:
            print("================")
            print(" +----+")
            print(" |    |")
            print(" o    |")
            print("/|    |")
            print("      |")
            print(self.__cadena)
            str = f"================\n+----+\n |    |\n o    |\n/|    |\n      |\n {self.__cadena}"
            return str

        elif vidas==2:
            print("================")
            print(" +----+")
            print(" |    |")
            print(" o    |")
            print("/|\   |")
            print("      |")
            print(self.__cadena)
            str = f"================\n+----+\n |    |\n o    |\n/|\   |\n      |\n {self.__cadena}"
            return str

        elif vidas==1:
            print("================")
            print(" +----+")
            print(" |    |")
            print(" o    |")
            print("/|\   |")
            print("/     |")
            print(self.__cadena)
            str = f"================\n+----+\n |    |\n o    |\n/|\   |\n/     |\n {self.__cadena}"
            return str

        elif vidas==0:
            print("================")
            print(" +----+")
            print(" |    |")
            print(" o    |")
            print("/|\   |")
            print("/ \   |")
            print(f"Has perdido, la palabra correcta era {palabra_buscada}")
            str = f"================\n+----+\n |    |\n o    |\n/|\   |\n/\    |\n Has perdido, la palabra correcta era {palabra_buscada}"
            return str
