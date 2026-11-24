import cv2
import numpy as np
import streamlit as st
from PIL import Image

st.title("Atv 5: HSV e recorte")
foto = Image.open("imagens/foto.jpg").convert("RGB")
img = np.array(foto)

# 1. HSV
st.header("1. HSV")
col1, col2 = st.columns(2)
hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
h, s, v = cv2.split(hsv)
with col1:
    st.image(img, caption="Foto original")
    st.write("No OpenCV: H vai de 0 a 179, S e V de 0 a 255.")
with col2:
    st.image(h, caption="H (matiz)")
    st.image(s, caption="S (saturação)")
    st.image(v, caption="V (brilho)")

# 2. Mudando o HSV
st.header("2. Mudando o HSV")
col1, col2 = st.columns(2)
with col1:
    desloca_h = st.slider("Deslocar matiz", 0, 179, 0)
    fator_s = st.slider("Fator de saturação", 0.0, 2.0, 1.0)
    fator_v = st.slider("Fator de brilho", 0.0, 2.0, 1.0)
with col2:
    novo_h = ((h.astype(int) + desloca_h) % 180).astype(np.uint8)
    novo_s = np.clip(s * fator_s, 0, 255).astype(np.uint8)
    novo_v = np.clip(v * fator_v, 0, 255).astype(np.uint8)
    novo = cv2.cvtColor(cv2.merge([novo_h, novo_s, novo_v]), cv2.COLOR_HSV2RGB)
    st.image(novo, caption="Foto com HSV alterado")

# 3. Faixa na escala
st.header("3. Faixa na escala")
col1, col2 = st.columns(2)
with col1:
    h_min, h_max = st.slider("Faixa de matiz (H)", 0, 179, (35, 85))
    s_min = st.slider("Saturação mínima", 0, 255, 50)
    v_min = st.slider("Brilho mínimo", 0, 255, 50)
with col2:
    escala_h = np.tile(np.arange(180, dtype=np.uint8), (30, 1))
    escala_hsv = cv2.merge([escala_h, np.full_like(escala_h, 255), np.full_like(escala_h, 255)])
    escala = cv2.cvtColor(escala_hsv, cv2.COLOR_HSV2RGB)
    fora = (escala_h < h_min) | (escala_h > h_max)
    escala[fora] = escala[fora] // 4
    st.image(escala.repeat(3, axis=1), caption=f"Escala de H: faixa {h_min} a {h_max}")

# 4. Máscara de cor
st.header("4. Máscara de cor")
col1, col2 = st.columns(2)
baixo = np.array([h_min, s_min, v_min])
alto = np.array([h_max, 255, 255])
mascara = cv2.inRange(hsv, baixo, alto)
with col1:
    st.image(mascara, caption="Máscara (branco = dentro da faixa)")
with col2:
    so_cor = cv2.bitwise_and(img, img, mask=mascara)
    st.image(so_cor, caption="Só a cor escolhida")

# 5. Recorte
st.header("5. Recorte")
col1, col2 = st.columns(2)
altura, largura = img.shape[:2]
with col1:
    x0, x1 = st.slider("Faixa em x", 0, largura, (largura // 4, 3 * largura // 4))
    y0, y1 = st.slider("Faixa em y", 0, altura, (altura // 4, 3 * altura // 4))
    marcada = img.copy()
    cv2.rectangle(marcada, (x0, y0), (x1, y1), (255, 0, 0), max(2, largura // 200))
    st.image(marcada, caption="Área do recorte")
with col2:
    recorte = img[y0:y1, x0:x1]
    if recorte.size > 0:
        st.image(recorte, caption=f"Recorte {x1 - x0}x{y1 - y0}")
    else:
        st.write("Recorte vazio.")

# 6. Espelhamento
st.header("6. Espelhamento")
col1, col2 = st.columns(2)
with col1:
    st.image(cv2.flip(img, 1), caption="Espelhada na horizontal")
with col2:
    st.image(cv2.flip(img, 0), caption="Espelhada na vertical")
