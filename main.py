import flet as ft

from Widgets.CampoDeTexto import CampoDeTexto
from Widgets.MenuPrincipalView import MenuPrincipal

'''
    La aplicacion principal llama a la vista principal
'''
def main(page):
    def poner_letra_clicl(e):
            txt_name = ft.TextField(label="Introduce una letra")        
            if not txt_name.value:
                txt_name.error_text = "Please enter your name"
                page.update()
            else:
                name = txt_name.value
                page.clean()
                page.add(ft.Text(f"Hello, {name}!"))
    txt_name = ft.TextField(label="Your name")
    page.add(txt_name, ft.ElevatedButton("Say hello!", on_click=poner_letra_clicl))

if __name__ == '__main__':

    ft.app(target=main)
