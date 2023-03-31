import streamlit as st

def main():
    st.title("Simple Chat App")
    st.write("Escribe un mensaje y la respuesta será siempre 'hola chat'.")

    user_input = st.text_input("Escribe tu mensaje aquí:")
    if user_input:
        st.write("Respuesta: hola chat")

if __name__ == "__main__":
    main()

