import flet as ft 
from flet import colors 

def converter_metros(valor,unidade_origem,unidade_destino):
    # Dicionário com fatores de conversão para metros
    unidades = {
        "metros": 1.0,
        "quilômetros": 1000.0,
        "milhas": 1609.34,
        "pés": 0.3048
    }
    # Verificar se as unidades fornecidas são válidas
    if unidade_destino not in unidades or unidade_destino not in unidades:
        raise ValueError("Unidade invalida")
    
    # Converter valor para metros
    valor_metros = valor * unidades[unidade_origem]

    valor_convertido = valor_metros / unidades[unidade_destino]
    return valor_convertido

def main(page:ft.Page):
    page.title = 'Conversor de unidades'
    page.window_width = 400
    page.window_height = 500
    page.bgcolor = colors.RED_ACCENT_100
    
    # Campo de entrada para o valor
    valor_input = ft.TextField(label='Valor',width=250)

    # Dropdown para selecionar a unidade de origem
    unidade_origem_dropdown = ft.Dropdown(
        label="Unidade de Origem",
        options=[
            ft.dropdown.Option("metros"),
            ft.dropdown.Option("quilômetros"),
            ft.dropdown.Option("milhas"),
            ft.dropdown.Option("pés")
        ],
        width=200
    )
    # Dropdown para selecionar a unidade de destino
    unidade_destino_dropdown = ft.Dropdown(
        label="Unidade de Destino",
        options=[
            ft.dropdown.Option("metros"),
            ft.dropdown.Option("quilômetros"),
            ft.dropdown.Option("milhas"),
            ft.dropdown.Option("pés")
        ],
        width=200
    )

    #Texto para exibir o resultado
    resultado_output = ft.Text("Resultado: ",size=20, weight="bold")

    # Função que será chamada ao clicar no botão de conversão
    def converter_click(e):
        try:
            valor = float(valor_input.value)
            unidade_origem = unidade_origem_dropdown.value
            unidade_destino = unidade_destino_dropdown.value
            
            resultado = converter_metros(valor, unidade_origem, unidade_destino)
            resultado_output.value = f"Resultado: {valor} {unidade_origem} = {resultado:.2f} {unidade_destino}"
        except ValueError as ve:
            resultado_output.value = f"Erro: {str(ve)}"
        page.update()

    # Botão para iniciar a conversão
    converter_button = ft.ElevatedButton("Converter", on_click=converter_click)

    page.add(
        valor_input,
        unidade_origem_dropdown,
        unidade_destino_dropdown,
        converter_button,
        resultado_output
    )
    
ft.app(target=main)
