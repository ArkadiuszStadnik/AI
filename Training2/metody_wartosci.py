import streamlit as st
from PIL import Image

def przekaz_dane(a, b):
    a = a + 1
    b = b + 1
    return a, b


if __name__ == '__main__':
    a = 11
    b = 0
    nowa_a, nowa_b = przekaz_dane(a, b)
    print(nowa_a, nowa_b)


image = Image.open('/home/student/PycharmProjects/AIProject/garfield.jpeg')


col1, col2 = st.columns(2)

with col1:
    st.header("Kolumna 1")
    st.write(nowa_a)
    st.image(image, caption='Garfield',use_column_width=True)

with col2:
    st.header("Kolumna 2")
    st.write(nowa_b)
    with st.expander("Wiecej informacji o Grafield"):
        st.write("Garfield to kot")
        st.write("Garfield ma 9 zyc")
        st.write("Garfield jest leniwy")