import flet as ft


from Ahorcado.AhorcadoModel import AhorcadoModel
from Ahorcado.AhorcadoView import AhorcadoView
from Widgets.CampoDeTexto import CampoDeTexto
from Widgets.MenuPrincipalView import MenuPrincipal
from Widgets.VistaAhorcado import VistaAhorcado

'''
    La aplicacion principal llama a la vista principal
'''
def main(page: ft.Page):
    page.adaptive = True
    path="./data/palabras.txt"
    VIDA = 6    
    model=AhorcadoModel(path=path, vida=VIDA)
    model.elegir_palabra()
    viewTerminal = AhorcadoView()
    viewTerminal.preparar_juego_visual(model.get_palabra_elegida())
    model.registrar_nuevo_observador(viewTerminal)
    
    page.title = "Ahorcado POO"
    campo_de_ahorcado = VistaAhorcado(text=viewTerminal.dibujar_ahorcado(model.get_vida(),model.get_palabra_elegida()))
    
    page.add(campo_de_ahorcado)
    
    page.add(ft.SafeArea(ft.Text("Ahoracado POO")))
    
    campo_de_texto = CampoDeTexto(page=page,model=model,view=campo_de_ahorcado, viewTerminal= viewTerminal)    
    page.add(campo_de_texto.build())

if __name__ == '__main__':
    ft.app(target=main)
