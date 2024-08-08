import flet as ft
import random

def main(page: ft.Page):
    # Configurações da página
    page.title = "Jogo de Adivinhação"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # Variáveis globais
    target_number = random.randint(0, 100)
    user_attempts = 0
    ranking = []

    # Função para atualizar o ranking com animação
    def update_ranking():
        sorted_ranking = sorted(ranking, key=lambda x: x['attempts'])
        ranking_container.controls.clear()
        for i, player in enumerate(sorted_ranking):
            player_text = ft.Text(f"{i + 1}. {player['name']} - {player['attempts']} tentativas", size=16)
            if player['name'] == player_name.value:
                player_text.color = ft.colors.GREEN
            ranking_container.controls.append(ft.Container(content=player_text, padding=5, animate=ft.Animation(600, ft.AnimationCurve.EASE_IN_OUT)))
        page.update()

    # Função para submeter o palpite
    def guess_number(e):
        nonlocal user_attempts, target_number

        if not input_box.value.isdigit():
            result_text.value = "Por favor, insira um número válido."
            page.update()
            return
        
        user_guess = int(input_box.value)
        user_attempts += 1
        
        if user_guess == target_number:
            result_text.value = "Parabéns! Você acertou!"
            target_number = random.randint(0, 100)  # Gera novo número

            # Verifica se o jogador já está no ranking
            for player in ranking:
                if player['name'] == player_name.value:
                    if user_attempts < player['attempts']:
                        player['attempts'] = user_attempts  # Atualiza se tiver menos tentativas
                    break
            else:
                # Se for a primeira vez do jogador, adiciona ao ranking
                ranking.append({"name": player_name.value, "attempts": user_attempts})

            # Reseta as tentativas para o próximo jogador
            user_attempts = 0
        elif user_guess < target_number:
            result_text.value = "Seu chute foi menor que o número alvo."
        else:
            result_text.value = "Seu chute foi maior que o número alvo."

        attempts_text.value = f"Tentativas: {user_attempts}"
        input_box.value = ""  # Limpa a caixa de entrada
        update_ranking()

    # Elementos da interface
    player_name = ft.TextField(label="Nome do Jogador", width=300)
    input_box = ft.TextField(label="Chute um número entre 0 e 100", width=300)
    submit_button = ft.ElevatedButton(text="Enviar", on_click=guess_number, width=150, bgcolor=ft.colors.BLUE, color=ft.colors.WHITE)
    result_text = ft.Text(size=20, color=ft.colors.ORANGE)
    attempts_text = ft.Text(f"Tentativas: {user_attempts}", size=18, color=ft.colors.YELLOW)
    ranking_title = ft.Text("Ranking", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.CYAN)
    ranking_container = ft.Column()

    # Layout principal
    page.add(
        ft.Column(
            [
                ft.Container(content=ft.Text("Jogo de Adivinhação", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.CYAN), padding=20),
                player_name,
                input_box,
                submit_button,
                result_text,
                attempts_text,
                ft.Divider(height=20, thickness=2),
                ranking_title,
                ranking_container
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# Inicia a aplicação Flet
ft.app(target=main)
