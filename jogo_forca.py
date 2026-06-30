import random
import time
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

# =========================
# LISTA DE PALAVRAS
# =========================
lista_palavras = [
    "PYTHON",
    "ALGORITMO",
    "ESTRUTURA",
    "DESENVOLVEDOR",
    "PROGRAMACAO",
    "COMPUTADOR",
    "TECNOLOGIA",
    "INTERFACE",
    "LOGICA",
    "SOFTWARE"
]

# =========================
# FORCA VISUAL
# =========================
estagios_forca = [
    """
     ┌───────┐
     │       │
             │
             │
             │
             │
    ═════════════
    """,
    """
     ┌───────┐
     │       │
     O       │
             │
             │
             │
    ═════════════
    """,
    """
     ┌───────┐
     │       │
     O       │
     |       │
             │
             │
    ═════════════
    """,
    """
     ┌───────┐
     │       │
     O       │
    /|       │
             │
             │
    ═════════════
    """,
    """
     ┌───────┐
     │       │
     O       │
    /|\\      │
             │
             │
    ═════════════
    """,
    """
     ┌───────┐
     │       │
     O       │
    /|\\      │
    /        │
             │
    ═════════════
    """,
    """
     ┌───────┐
     │       │
     O       │
    /|\\      │
    / \\      │
             │
    ═════════════
    """
]

# =========================
# BANNER DO JOGO
# =========================
def exibir_banner():
    print(Fore.CYAN + "=" * 60)
    print(Fore.MAGENTA + Style.BRIGHT + "🎮 FORCA PREMIUM - PYTHON EDITION 🎮")
    print(Fore.CYAN + "=" * 60)
    print(Fore.YELLOW + "Descubra a palavra antes que a forca seja completada!")
    print(Fore.YELLOW + "Boa sorte, jogador 😄")
    print(Fore.CYAN + "=" * 60)


# =========================
# EFEITO DE CARREGAMENTO
# =========================
def carregamento():
    print(Fore.BLUE + "\nInicializando sistema", end="")

    for _ in range(3):
        time.sleep(0.6)
        print(Fore.BLUE + ".", end="")

    print(Fore.GREEN + "\nSistema carregado com sucesso!\n")
    time.sleep(1)


# =========================
# ESCOLHER DIFICULDADE
# =========================
def escolher_dificuldade():
    print(Fore.CYAN + "\nSelecione a dificuldade:")
    print(Fore.GREEN + "1 - Fácil")
    print(Fore.YELLOW + "2 - Médio")
    print(Fore.RED + "3 - Difícil")

    while True:
        escolha = input(Fore.WHITE + "\nDigite a opção desejada: ")

        if escolha == "1":
            return 8

        elif escolha == "2":
            return 6

        elif escolha == "3":
            return 4

        else:
            print(Fore.RED + "Opção inválida. Tente novamente.")


# =========================
# INICIAR JOGO
# =========================
def iniciar_jogo():
    palavra_secreta = random.choice(lista_palavras)

    palavra_oculta = ["_"] * len(palavra_secreta)

    letras_tentadas = set()

    tentativas = escolher_dificuldade()

    pontuacao = 0

    return (
        palavra_secreta,
        palavra_oculta,
        letras_tentadas,
        tentativas,
        pontuacao
    )


# =========================
# EXIBIR STATUS
# =========================
def exibir_status(
    palavra_oculta,
    letras_tentadas,
    tentativas,
    pontuacao
):

    print(Fore.CYAN + estagios_forca[6 - tentativas])

    print(
        Fore.WHITE +
        "\nPalavra: " +
        " ".join(palavra_oculta)
    )

    print(
        Fore.YELLOW +
        "Letras utilizadas: " +
        ", ".join(sorted(letras_tentadas))
    )

    print(
        Fore.GREEN +
        f"Pontuação: {pontuacao}"
    )

    print(
        Fore.RED +
        f"Tentativas restantes: {tentativas}"
    )


# =========================
# PROCESSAR TENTATIVA
# =========================
def processar_tentativa(
    letra,
    palavra_secreta,
    palavra_oculta,
    letras_tentadas,
    tentativas,
    pontuacao
):

    if letra in letras_tentadas:
        print(Fore.YELLOW + "\n⚠ Você já utilizou essa letra.")
        return palavra_oculta, tentativas, pontuacao

    letras_tentadas.add(letra)

    if letra in palavra_secreta:

        print(Fore.GREEN + "\n✅ Excelente! Letra correta.")

        for indice in range(len(palavra_secreta)):

            if palavra_secreta[indice] == letra:
                palavra_oculta[indice] = letra
                pontuacao += 10

    else:
        tentativas -= 1
        pontuacao -= 5

        print(Fore.RED + "\n❌ Letra incorreta!")

    return palavra_oculta, tentativas, pontuacao


# =========================
# JOGAR NOVAMENTE
# =========================
def jogar_novamente():

    resposta = input(
        Fore.CYAN +
        "\nDeseja jogar novamente? (S/N): "
    ).upper()

    return resposta == "S"


# =========================
# INÍCIO DO SISTEMA
# =========================
exibir_banner()

carregamento()

while True:

    (
        palavra_secreta,
        palavra_oculta,
        letras_tentadas,
        tentativas,
        pontuacao

    ) = iniciar_jogo()

    while tentativas > 0 and "_" in palavra_oculta:

        print(Fore.MAGENTA + "\n" + "-" * 60)

        exibir_status(
            palavra_oculta,
            letras_tentadas,
            tentativas,
            pontuacao
        )

        letra = input(
            Fore.WHITE +
            "\nDigite uma letra: "
        ).upper()

        # Validação
        if len(letra) != 1 or not letra.isalpha():

            print(
                Fore.RED +
                "\n⚠ Entrada inválida. Digite apenas uma letra."
            )

            continue

        (
            palavra_oculta,
            tentativas,
            pontuacao

        ) = processar_tentativa(
            letra,
            palavra_secreta,
            palavra_oculta,
            letras_tentadas,
            tentativas,
            pontuacao
        )

    print(Fore.CYAN + "\n" + "=" * 60)

    # VITÓRIA
    if "_" not in palavra_oculta:

        print(Fore.GREEN + Style.BRIGHT)
        print("🏆 PARABÉNS! VOCÊ VENCEU! 🏆")
        print(f"A palavra secreta era: {palavra_secreta}")
        print(f"Pontuação final: {pontuacao}")

    # DERROTA
    else:

        print(Fore.RED + estagios_forca[6])

        print(Fore.RED + Style.BRIGHT)
        print("💀 GAME OVER 💀")
        print(f"A palavra secreta era: {palavra_secreta}")
        print(f"Pontuação final: {pontuacao}")

    print(Fore.CYAN + "=" * 60)

    if not jogar_novamente():

        print(
            Fore.MAGENTA +
            "\nObrigado por jogar Forca Premium! 🚀"
        )

        break