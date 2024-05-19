import flet as ft


from Ahorcado.AhorcadoModel import AhorcadoModel
from Ahorcado.AhorcadoView import AhorcadoView
from Widgets.AhorcadoWidget import AhorcadoWidget
from Widgets.CampoDeTextoWidget import CampoDeTextoWidget

"""
    La aplicacion principal llama a la vista principal
"""


def main(page: ft.Page):
    page.adaptive = True
    path = "./data/palabras.txt"
    VIDA = 6
    model = AhorcadoModel(path=path, vida=VIDA)
    model.elegir_palabra()
    viewTerminal = AhorcadoView()
    viewTerminal.preparar_juego_visual(model.get_palabra_elegida())
    model.registrar_nuevo_observador(viewTerminal)

    page.title = "Ahorcado POO"
    
    # Inicia la partida y necesitamos previsualizar el ahorcado
    
    visual_ahorcado_widget = AhorcadoWidget(
        text=viewTerminal.dibujar_ahorcado(
            model.get_vida(), model.get_palabra_elegida()
        ),view=viewTerminal
    )
    page.add(visual_ahorcado_widget)
    #Inicializacmos el campo de texto y lo añadimos a la pantalla
    campo_de_texto_widget = CampoDeTextoWidget(model=model,ahorcado_dibujado=visual_ahorcado_widget)
    page.add(campo_de_texto_widget)

if __name__ == "__main__":
    ft.app(target=main)
