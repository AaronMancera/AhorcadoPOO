import flet as ft

from Ahorcado.AhorcadoModel import AhorcadoModel
from Widgets.AhorcadoWidget import AhorcadoWidget


class CampoDeTextoWidget(ft.Card):
    def __init__(self, model: AhorcadoModel, ahorcado_dibujado: AhorcadoWidget):
        """Genera un widget de campo de texto para introducir una letra y que este relacionado con el widget del ahorcado

        Args:
            model (AhorcadoModel): el modelo del ahorcado
            ahorcado_dibujado (AhorcadoWidget): el widget donde se dibuja el ahorcado
        """
        super().__init__()
        self.model = model
        self.ahorcado_dibujado = ahorcado_dibujado
        self.txt_name = ft.TextField(label="Introduce una letra")
        self.content = ft.ResponsiveRow(
            controls=[
                ft.Container(
                    content=self.txt_name,
                    col={"md":12,"lg":6}
                ),
                ft.Container(                
                    col={"md":12,"lg":6},
                    content=ft.TextButton(                        
                        text="Aceptar",
                        on_click=self.comprobar_texto,
                        height=60
                    ),
                    
                ),
            ]
        )

    def update(self):
        """El update actualizara el campo de texto. Pero tenemos un if que si el jugador ya ha perdido o ha terminado
        se quitara el boton y el espacio para escribir
        Returns:
            Devuelve el mimso, con la modificacion que le hacemos antes.
        """
        if self.model.get_vida() == 0:
            self.content = ft.Text("Has perdido")
        elif self.model.palabra_es_acertada():
            self.content = ft.Text("Has ganado")
        return super().update()

    def comprobar_texto(self, e):
        """Comprueba el texto que ha sido ingresado y revisa que sea una unica letra. Posteriormente revisara si ya ha sido introducido y aplicara los cambios en las vistas
        Args:
            e (_type_): Exception que se pasa por parametro
        """
        if str(self.txt_name.value) == "" or len(str(self.txt_name.value)) > 2:
            self.txt_name.error_text = "Introduce una letra"
            self.update()
        else:
            if self.model.letra_no_ha_sido_escrita(str(self.txt_name.value)):
                self.avanzar_partida()
            self.txt_name.error_text = ""
            self.txt_name.value = ""
            self.update()

    def avanzar_partida(self):
        """Metodo que hace avanzar la partida en los valores del juego y visualmente"""
        self.model.letra_en_la_palabra(self.txt_name.value)
        self.ahorcado_dibujado.avanzar_partida(
            vidas=self.model.get_vida(), palabra=self.model.get_palabra_elegida()
        )
