import streamlit as st
import numpy as np

def inicio():
    st.title("Computação Gráfica")
    st.write("Meu nome é Clara.")
    n = st.slider("Tamanho", 2, 64, 8)
    img = np.random.randint(0, 256, (n, n), dtype=np.uint8)
    st.image(img, caption=f"Imagem {n}x{n}", width=300)
    st.write(img)


pagina = st.navigation([
    st.Page(inicio, title="Início"),
    st.Page("src/atv2.py", title="Atividade 2 — Bandeira"),
    st.Page("src/atv3.py", title="Atividade 3 — Padrão"),
])
pagina.run()
