import flet as ft
from View.Views import Views

"""
    La aplicacion principal llama a la vista principal
"""


def main(page: ft.Page):
    page.title = "Ahorcado POO"
    page.window_center=True
    page.window_min_width = 640
    page.window_min_height = 640
    page.window_to_front = True
    router = Views(page=page)
    page.on_route_change = router.route_change
    page.add(
        #Este tiene que ser responsivero, ya que como es el el resto se va a sobrescribir a este
        ft.ResponsiveRow(
            [
                router.body,
            ],
            expand=True,
        )
    )

    page.go('/')
    page.update()
# def juego(page:ft.Page):
#     page.adaptive = True
#     path = "./data/palabras.txt"
#     VIDA = 6
#     model = AhorcadoModel(path=path, vida=VIDA)
#     model.elegir_palabra()
#     viewTerminal = AhorcadoView()
#     viewTerminal.preparar_juego_visual(model.get_palabra_elegida())
#     model.registrar_nuevo_observador(viewTerminal)

#     page.title = "Ahorcado POO"
    
#     # Inicia la partida y necesitamos previsualizar el ahorcado
    
#     visual_ahorcado_widget = AhorcadoWidget(
#         text=viewTerminal.dibujar_ahorcado(
#             model.get_vida(), model.get_palabra_elegida()
#         ),view=viewTerminal
#     )
#     page.add(visual_ahorcado_widget)
#     #Inicializacmos el campo de texto y lo añadimos a la pantalla
#     campo_de_texto_widget = CampoDeTextoWidget(model=model,ahorcado_dibujado=visual_ahorcado_widget)
#     page.add(campo_de_texto_widget)

if __name__ == "__main__":
    ft.app(target=main)
