import random


class AhorcadoModel:
    #Constructor
    def __init__(self, path,vida):
        self.__path = path
        self.__vida = vida
        self.__palabras_elegida = ""
        self.__letras_acertadas = 0
        self.__letras_ya_escritas = []
        self.__observadores = []
        
    def elegir_palabra(self):
        with open(self.__path,encoding="utf-8") as file:
            palabras=[]
            for linea in file:
                palabras.append(linea)
                #print(linea)
        self.__palabras_elegida=palabras[random.randint(0,len(palabras)-1)].replace("\n", "")
    
    def letra_en_la_palabra(self, letra):
        if letra in self.__palabras_elegida:
            # print(letra in palabraResolver)         
            # list(self.__palabrasElegida).index(letra)
            # self.__letras_acertadas+=1
            index = 0
            while index < len(self.__palabras_elegida):
                index = self.__palabras_elegida.find(letra,index)
                if index == -1:
                    break
                self.__letras_acertadas+=1                
                index+=1
            self.__notify_observers(letra=letra)
        else:
            self.__perder_una_vida()
    
    def palabra_es_acertada(self):
        if self.__letras_acertadas == len(self.__palabras_elegida):
            return True
        else:
            return False

    def sin_vidas(self):
        if(self.__vida<=0):
            return True
        else:
            return False

    def letra_no_ha_sido_escrita(self,letra):
        if letra in self.__letras_ya_escritas:
            return False
        else:
            self.__letras_ya_escritas.append(letra)
            return True

    def __perder_una_vida(self):
        self.__vida -=1
    #Aplicacion de metodo observer
    def registrar_nuevo_observador(self, observador):
        self.__observadores.append(observador)

    def del_observador(self, observador):
        self.__observadores.remove(observador)

    def __notify_observers(self, letra):
        for observador in self.__observadores:
            observador.actualizar_cadena(self.__palabras_elegida, letra)

    #getters
    def get_palabra_elegida(self):
        return self.__palabras_elegida

    def get_vida(self):
        return self.__vida