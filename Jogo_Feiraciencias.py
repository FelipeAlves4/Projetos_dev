import flet as ft
import random

def main(page: ft.Page):
    # Configurações da página
    page.title = "Desafio do Código: Humano vs Máquina"
    page.theme_mode = ft.ThemeMode.DARK
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.padding = 20

    # Fundo gradiente
    page.bgcolor = ft.LinearGradient(
        colors=[ft.colors.DEEP_PURPLE, ft.colors.INDIGO, ft.colors.BLUE],
        begin=ft.alignment.top_left,
        end=ft.alignment.bottom_right,
    )

    # Variáveis globais
    target_number = random.randint(0, 100)
    user_attempts = 0
    ranking = []

    # Função para atualizar o ranking com animação
    def update_ranking():
        sorted_ranking = sorted(ranking, key=lambda x: x['attempts'])
        ranking_container.controls.clear()
        for i, player in enumerate(sorted_ranking):
            player_text = ft.Text(f"{i + 1}. {player['name']} - {player['attempts']} tentativas",
                                  size=16,
                                  weight=ft.FontWeight.BOLD,
                                  color=ft.colors.WHITE)
            if player['name'] == player_name.value:
                player_text.color = ft.colors.LIME_ACCENT
            ranking_container.controls.append(
                ft.Container(
                    content=player_text,
                    padding=5,
                    border_radius=ft.border_radius.all(10),
                    bgcolor=ft.colors.TRANSPARENT,
                    animate=ft.Animation(600, ft.AnimationCurve.EASE_IN_OUT)
                )
            )
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
            result_text.color = ft.colors.LIME_ACCENT
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
            result_text.color = ft.colors.AMBER
        else:
            result_text.value = "Seu chute foi maior que o número alvo."
            result_text.color = ft.colors.RED_ACCENT

        attempts_text.value = f"Tentativas: {user_attempts}"
        input_box.value = ""  # Limpa a caixa de entrada
        update_ranking()

    # Elementos da interface
    player_name = ft.TextField(label="Nome do Jogador", width=300, color=ft.colors.WHITE)
    input_box = ft.TextField(label="Chute um número entre 0 e 100", width=300, color=ft.colors.WHITE)
    submit_button = ft.ElevatedButton(
        text="Enviar",
        on_click=guess_number,
        width=150,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            bgcolor=ft.colors.BLUE_GREY,
            color=ft.colors.WHITE,
            elevation=10,
        )
    )
    result_text = ft.Text(size=20, weight=ft.FontWeight.BOLD, color=ft.colors.WHITE)
    attempts_text = ft.Text(f"Tentativas: {user_attempts}", size=18, color=ft.colors.WHITE)
    ranking_title = ft.Text("Ranking", size=24, weight=ft.FontWeight.BOLD, color=ft.colors.CYAN)
    ranking_container = ft.Column()

    # Layout principal
    page.add(
        ft.Column(
            [
                ft.Container(
                    content=ft.Text("Desafio do Código: Humano vs Máquina", size=30, weight=ft.FontWeight.BOLD, color=ft.colors.LIME_ACCENT),
                    padding=20,
                    alignment=ft.alignment.center
                ),
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
