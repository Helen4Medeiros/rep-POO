import streamlit as st
from datetime import datetime
from paciente import Paciente

class PacienteUI:
    def main():
        st.header('Dados do Paciente')
        nome = st.text_input('Nome')
        cpf = st.text_input('CPF')
        fone = st.text_input('Telefone')
        nascimento = st.text_input('Nascimento')
        if st.button('Idade'):
            n = str(nome)
            c = str(cpf)
            f = str(fone)
            nasc = datetime.strptime(nascimento, '%d/%m/%Y')
            p = Paciente(n, c, f, nasc)
            # st.write(p)
            st.write(p.idade())
