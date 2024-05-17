import flet as ft

class CampoDeTexto:
    def poner_letra_clicl(e):
        txt_name = ft.TextField(label="Introduce una letra")        
        if not txt_name.value:
            txt_name.error_text = "Please enter your name"
            page.update()
        else:
            name = txt_name.value
            page.clean()
            page.add(ft.Text(f"Hello, {name}!"))