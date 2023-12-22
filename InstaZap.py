import flet as ft
import pyperclip as pc

def main(pagina: ft.Page):
    pagina.title = "InstaZap"
    # pagina.vertical_alignment = ft.MainAxisAlignment.CENTER
    # pagina.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    dlg = ft.AlertDialog(
        title=ft.Text("Você digitou um telefone incorreto!")
    )
    copiado = ft.AlertDialog(title=ft.Text("Copiado com Sucesso!"))

    def open_dlg(dlg):
        pagina.dialog = dlg
        dlg.open = True
        pagina.update()

    # funções
    def redirecionar_contato(e):
        pass

    def redirecionar_app(e):
        pass

    def gerar_link(e):
        whatsapp = "https://api.whatsapp.com/send?phone=55"
        try:
            num_whatsApp.value = int(num_whatsApp.value)
        except:
            # if(num_whatsApp.value == "" or type(num_whatsApp.value) == str):
            open_dlg(dlg=dlg)
        else:
            link = str(num_whatsApp.value)
            whatsapp += link
            link_whatsApp.value = whatsapp

        pagina.update()

    def copiar_link(e):
        pc.copy(link_whatsApp.value)
        open_dlg(copiado)

    # criar os itens que queremos na página!
    num_whatsApp = ft.TextField(label="Número WhatsApp:")
    btn_gerar_link = ft.ElevatedButton(text="Gerar Link", on_click=gerar_link)
    link_whatsApp = ft.TextField(label="Link")
    btn_copiar = ft.ElevatedButton(text="Copiar Link", on_click=copiar_link)

    pagina.add(
        num_whatsApp, link_whatsApp,  ft.Row(
            [btn_gerar_link, btn_copiar], alignment=ft.MainAxisAlignment.CENTER)
    )


ft.app(target=main)

