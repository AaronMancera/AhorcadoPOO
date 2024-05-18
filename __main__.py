import flet as ft


from Ahorcado.AhorcadoModel import AhorcadoModel
from Ahorcado.AhorcadoView import AhorcadoView
from Widgets.CampoDeTexto import CampoDeTexto
from Widgets.MenuPrincipalView import MenuPrincipal

'''
    La aplicacion principal llama a la vista principal
'''
def main(page: ft.Page):
    path="./data/palabras.txt"
    VIDA = 6    
    model=AhorcadoModel(path=path, vida=VIDA)
    model.elegir_palabra()
    view = AhorcadoView()
    view.preparar_juego_visual(model.get_palabra_elegida())    
    model.registrar_nuevo_observador(view)
    
    page.title = "Ahorcado POO"
    page.add(ft.SafeArea(ft.Text("Ahoracado POO")))
    
    campo_de_texto = CampoDeTexto(page=page,model=model,view=view)    
    page.add(campo_de_texto.build())

if __name__ == '__main__':
    ft.app(target=main)
