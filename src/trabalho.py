import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Trabalho de Computação Gráfica")

st.header("1. Saturação")
foto = Image.open("imagens/foto.jpg").convert("RGB")
img = np.array(foto)
fator_s = st.slider("Fator de saturação", 0.0, 2.0, 1.0)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(hsv)
novo_s = np.clip(s * fator_s, 0, 255).astype(np.uint8)
resultado = cv2.cvtColor(cv2.merge([h, novo_s, v]), cv2.COLOR_HSV2RGB)
st.image(resultado, caption=f"Saturação × {fator_s}")

st.header("2. Brilho")
foto = Image.open("imagens/foto.jpg").convert("RGB")
img = np.array(foto)
fator_v = st.slider("Fator de brilho", 0.0, 2.0, 1.0)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(hsv)
novo_v = np.clip(v * fator_v, 0, 255).astype(np.uint8)
resultado = cv2.cvtColor(cv2.merge([h, s, novo_v]), cv2.COLOR_HSV2RGB)
st.image(resultado, caption=f"Brilho × {fator_v}")

st.header("3. Matiz girada")
foto = Image.open("imagens/foto.jpg").convert("RGB")
img = np.array(foto)
giro = st.slider("Giro da matiz", 0, 179, 0)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(hsv)
novo_h = ((h.astype(int) + giro) % 180).astype(np.uint8)
resultado = cv2.cvtColor(cv2.merge([novo_h, s, v]), cv2.COLOR_HSV2RGB)
st.image(resultado, caption=f"Matiz girada em {giro}")

st.header("8. Negativo")
foto = Image.open("imagens/foto.jpg").convert("RGB")
img = np.array(foto)
negativo = 255 - img
col1, col2 = st.columns(2)
with col1:
    st.image(img, caption="Foto original")
with col2:
    st.image(negativo, caption="Negativo")

st.header("9. Recorte")
foto = Image.open("imagens/foto.jpg").convert("RGB")
img = np.array(foto)
altura, largura = img.shape[:2]
lado = st.slider("Lado do quadrado", 10, min(altura, largura) - 1, min(altura, largura) // 2)
x0 = st.slider("Coluna inicial", 0, largura - lado, 0)
y0 = st.slider("Linha inicial", 0, altura - lado, 0)
recorte = img[y0:y0 + lado, x0:x0 + lado]
st.image(recorte, caption=f"Recorte {lado}x{lado}")

st.header("11. Espelhamento")
foto = Image.open("imagens/foto.jpg").convert("RGB")
img = np.array(foto)
col1, col2 = st.columns(2)
with col1:
    st.image(cv2.flip(img, 1), caption="Espelhada na horizontal")
with col2:
    st.image(cv2.flip(img, 0), caption="Espelhada na vertical")
