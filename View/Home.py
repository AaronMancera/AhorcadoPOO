from typing import Any, List
import flet as ft


def Home(page):
    print("Inicia el home")
    bienvenida = ft.Column()
    bienvenida.controls.append(ft.Text("Bienvenido al juego del Ahorcado POO"))
    def btn_go_to_game(e):
        page.go("/game")
        page.update()
    bienvenida.controls.append(ft.ElevatedButton(text="Ir para el juego",on_click=btn_go_to_game))
    
    content = ft.Column(
        [
            bienvenida
        ]
    )
    return content
