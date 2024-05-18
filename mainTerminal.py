from Ahorcado.AhorcadoModel import AhorcadoModel
from Ahorcado.AhorcadoView import AhorcadoView

def ahorcado_terminal():
    VIDA = 6    
    path="./data/palabras.txt"
    model = AhorcadoModel(path=path, vida=VIDA)
    model.elegir_palabra()
    view = AhorcadoView()
    view.preparar_juego_visual(model.get_palabra_elegida())    
    model.registrar_nuevo_observador(view)
    while(model.palabra_es_acertada() == False and model.sin_vidas() ==False):
        view.dibujar_ahorcado(model.get_vida(),model.get_palabra_elegida())
        usuario=input("Escribe una letra: ")
        usuario = usuario.lower()    
        if(len(usuario)==0 or len(usuario) > 1 or (ord(usuario)<97 or ord(usuario)>122)):
            print("Error 00: La letra que has introducido no esta correcta")
            print("Revise que usted haya escrito solo un unico caracter")
            print("Revise que usted haya un caracter aA-zZ")
            input("Pulse intro para continuar")
        else:
            if(model.letra_no_ha_sido_escrita(letra=usuario)):
                model.letra_en_la_palabra(letra=usuario)
    view.dibujar_ahorcado(model.get_vida(),model.get_palabra_elegida())


ahorcado_terminal()