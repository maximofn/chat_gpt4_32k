#!/usr/bin/env python3
import sys
import subprocess
import platform
import re
import os

import subprocess

def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    import openai
except ImportError:
    install_package("openai")
    import openai

import streamlit as st

def main():
    st.title("Simple Chat App")
    st.write("Escribe un mensaje y la respuesta será siempre 'hola chat'.")

    user_input = st.text_input("Escribe tu mensaje aquí:")
    if user_input:
        st.write("Respuesta: hola chat")

if __name__ == "__main__":
    main()

