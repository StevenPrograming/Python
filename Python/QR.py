import flet as ft
import qrcode

#Para crear la ventana interfaz
def main(page: ft.page):

    #Funcion del boton
    def btn_click(e):
        codigo_qr = qrcode.QRCode(
            version=1,
            box_size=10,
            border=4
        )
        codigo_qr.add_data(texto.value)
        imagen_qr = codigo_qr.make_image(fill_color="black",
                                         background_color="white")
        imagen_qr.save("codigo_qr.png")

        imagen_col.controls.append (ft.Image(
                                                src=f"codigo_qr.png",
                                                width=400,
                                                height=400,
                                                fit=ft.ImageFit.CONTAIN,
                                            ))
        
        page.update()


    #controles de la aplicacion (Funciones)
    texto = ft.TextField(label = "Texto que deseas convertir")
    boton = ft.ElevatedButton("Generar")
    imagen_col = ft.Column(expand=1, wrap = False, scroll='AUTO')

    boton.on_click = btn_click

    #Codigo para que se vea en la interfaz
    page.add(texto,
             boton,
             imagen_col)

ft.app(target=main)