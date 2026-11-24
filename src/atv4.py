import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image

st.title("Atv 4: RGB")

# 1. Leitura da foto
st.header("1. Leitura da foto")
col1, col2 = st.columns(2)
foto = Image.open("imagens/foto.jpg").convert("RGB")
img = np.array(foto)
with col1:
    st.image(img, caption="Foto original")
with col2:
    altura, largura, canais = img.shape
    st.write(f"Altura: {altura} px")
    st.write(f"Largura: {largura} px")
    st.write(f"Canais: {canais}")
    st.write(f"Tipo: {img.dtype}")
    st.write("Pixel do centro (R, G, B):", img[altura // 2, largura // 2])

# 2. Canais
st.header("2. Canais")
col1, col2 = st.columns(2)
r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]
with col1:
    st.image(r, caption="Canal R (cinza)")
    st.image(g, caption="Canal G (cinza)")
    st.image(b, caption="Canal B (cinza)")
with col2:
    for i, nome in enumerate(["R", "G", "B"]):
        so_canal = np.zeros_like(img)
        so_canal[:, :, i] = img[:, :, i]
        st.image(so_canal, caption=f"Só o canal {nome}")

# 3. Cubo e BGR
st.header("3. Cubo e BGR")
col1, col2 = st.columns(2)
with col1:
    pixels = img.reshape(-1, 3)
    rng = np.random.default_rng(0)
    amostra = pixels[rng.choice(len(pixels), size=min(3000, len(pixels)), replace=False)]
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.scatter(amostra[:, 0], amostra[:, 1], amostra[:, 2], c=amostra / 255, s=4)
    ax.set_xlabel("R")
    ax.set_ylabel("G")
    ax.set_zlabel("B")
    ax.set_xlim(0, 255)
    ax.set_ylim(0, 255)
    ax.set_zlim(0, 255)
    st.pyplot(fig)
    st.caption("Pixels da foto no cubo RGB")
with col2:
    bgr = img[:, :, ::-1]
    st.image(bgr, caption="Canais trocados (BGR lido como RGB)")

# 4. Tons de cinza
st.header("4. Tons de cinza")
col1, col2 = st.columns(2)
with col1:
    media = img.mean(axis=2).astype(np.uint8)
    st.image(media, caption="Média (R + G + B) / 3")
with col2:
    pesos = np.array([0.299, 0.587, 0.114])
    luminancia = (img @ pesos).astype(np.uint8)
    st.image(luminancia, caption="Ponderada 0.299 R + 0.587 G + 0.114 B")
