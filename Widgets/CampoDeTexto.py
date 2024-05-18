import flet as ft


from Ahorcado.AhorcadoModel import AhorcadoModel
from Ahorcado.AhorcadoView import AhorcadoView

'''
Esta clase se encargara de controlar el campo de texto y el boton de poner letra
'''
class CampoDeTexto(ft.UserControl):
    #Para poder actualizar la camara necesitamos llevbarnos el la pagina
    def __init__(self, page:ft.Page, model:AhorcadoModel,view: AhorcadoView):
        super().__init__()
        self.VIDA = 6        
        self.page = page
        self.model = model
        self.view = view
    '''
    Esta funcion es la que se encarga de realizar la build, añadiendo el boton
    '''
    def build(self):
        self.view.dibujar_ahorcado(self.model.get_vida(),self.model.get_palabra_elegida())        
        self.txt_name = ft.TextField(label="Introduce una letra") 
        self.contenido = [
            ft.Row(
                spacing=5,controls=
                [                        
                    ft.Container( content=self.txt_name),
                    ft.Container(content=ft.ElevatedButton("Aceptar", on_click=self.poner_letra_click)),    
                                    
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
        ]
        return self.crear_boton()
    
    def crear_boton(self):
        return ft.Card(
            content=ft.Container(
                content=
                    ft.Column(
                        controls=self.contenido
                    )
            )
        )

    def poner_letra_click(self,e):
        print(len(str(self.txt_name.value)))
        if str(self.txt_name.value) == "" or len(str(self.txt_name.value)) > 2 :
            self.txt_name.error_text = "Introduce una letra"        
            self.page.update()
        else:
            if self.model.letra_no_ha_sido_escrita(str(self.txt_name.value)) :
                self.model.letra_en_la_palabra(self.txt_name.value)      
                self.view.dibujar_ahorcado(self.model.get_vida(),self.model.get_palabra_elegida())            
            self.txt_name.error_text = ""
            self.txt_name.value=""        
            self.page.update()