import flet as ft 
from flet import colors 
import random
import string

def gerar_senha(tamanho=12, incluir_maiusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_simbolos=True):
    caracteres = ''
    if incluir_maiusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation

    if caracteres == '':
        raise ValueError("Pelo menos um tipo de caractere deve ser selecionado")

    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha


def main(page:ft.Page):
    page.bgcolor = colors.AMBER_900
    page.window_resizable = False
    page.window_width = 350
    page.window_height = 400
    page.title =  "Gerador de Senha"
    page.window_always_on_top = True

    tamanho_input = ft.TextField(label="Tamanho da Senha", value="12", width=200)
    incluir_maiusculas_checkbox = ft.Checkbox(label="Incluir Letras Maiúsculas", value=True)
    incluir_minusculas_checkbox = ft.Checkbox(label="Incluir Letras Minúsculas", value=True)
    incluir_numeros_checkbox = ft.Checkbox(label="Incluir Números", value=True)
    incluir_simbolos_checkbox = ft.Checkbox(label="Incluir Símbolos", value=True)
    senha_output = ft.Text("Senha Gerada: ", size=20, weight="bold")

    def gerar_senha_click(e):
        try:
            tamanho = int(tamanho_input.value)
            incluir_maiusculas = incluir_maiusculas_checkbox.value
            incluir_minusculas = incluir_minusculas_checkbox.value
            incluir_numeros = incluir_numeros_checkbox.value
            incluir_simbolos = incluir_simbolos_checkbox.value

            senha = gerar_senha(tamanho, incluir_maiusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
            senha_output.value = f"Senha Gerada: {senha}"
            page.update()
        except ValueError as ve:
            senha_output.value = f"Erro: {str(ve)}"
            page.update()

    gerar_senha_button = ft.ElevatedButton("Gerar Senha", on_click=gerar_senha_click)

    page.add(
        tamanho_input,
        incluir_maiusculas_checkbox,
        incluir_minusculas_checkbox,
        incluir_numeros_checkbox,
        incluir_simbolos_checkbox,
        gerar_senha_button,
        senha_output,
    )


ft.app(target=main)
