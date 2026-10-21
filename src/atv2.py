import numpy as np
import streamlit as st


def ampliar(imagem, fator=12):
    """Amplia cada pixel sem suavizar suas bordas."""
    return np.repeat(np.repeat(imagem, fator, axis=0), fator, axis=1)


st.title("Atividade 2 - Bandeira em pixels")
st.write("Bandeira do Reino Unido")

# Cores RGB da referência, em hexadecimal para o seletor de cores.
azul_hex = st.color_picker("Azul", "#012169")
branco_hex = st.color_picker("Branco", "#FFFFFF")
vermelho_hex = st.color_picker("Vermelho", "#C8102E")


def rgb(cor):
    return tuple(int(cor[i:i + 2], 16) for i in (1, 3, 5))


azul = rgb(azul_hex)
branco = rgb(branco_hex)
vermelho = rgb(vermelho_hex)

# Matriz de 30 linhas por 50 colunas, com três canais de cor.
bandeira = np.zeros((30, 50, 3), dtype=np.uint8)
bandeira[:] = azul

# Diagonais brancas e vermelhas. O vermelho é deslocado em cada
# metade para reproduzir o desenho assimétrico da bandeira.
for linha in range(30):
    for coluna in range(50):
        x = coluna + 0.5
        y = linha + 0.5
        diagonal_1 = y - 0.6 * x
        diagonal_2 = y - (30 - 0.6 * x)
        if abs(diagonal_1) <= 3 or abs(diagonal_2) <= 3:
            bandeira[linha, coluna] = branco
        if coluna < 25:
            faixa_1 = 0 <= diagonal_1 <= 1.8
            faixa_2 = 0 <= diagonal_2 <= 1.8
        else:
            faixa_1 = -1.8 <= diagonal_1 <= 0
            faixa_2 = -1.8 <= diagonal_2 <= 0
        if faixa_1 or faixa_2:
            bandeira[linha, coluna] = vermelho

# Cruz branca e, por cima dela, a cruz vermelha central.
bandeira[10:20, :] = branco
bandeira[:, 20:30] = branco
bandeira[12:18, :] = vermelho
bandeira[:, 22:28] = vermelho

st.image(ampliar(bandeira), caption="Reino Unido — 50 × 30 pixels")
st.write(f"Cores RGB: azul {azul}, branco {branco}, vermelho {vermelho}.")
