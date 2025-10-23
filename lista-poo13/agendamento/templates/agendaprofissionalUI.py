import streamlit as st
import time
from datetime import datetime as dt
from views import View

class AgendaProfissional: 
    def main():
        st.header("Abrir Minha Agenda")
        data = st.text_input("Informe a data no formato DD/MM/AAAA", dt.now().strftime("%d/%m/%Y"))
        inicio = st.text_input("Informe o horário inicial no formato HH:MM", dt.now().strftime("%H:%M"))
        fim = st.text_input("Informe o horário final no formato HH:MM", dt.now().strftime("%H:%M"))
        intervalo = st.text_input("Informe o intervalo entre os horários (min)", "")
        if st.button("Abrir Agenda"):
            View.profissional_agenda(data, inicio, fim, int(intervalo), (st.session_state["usuario_id"]))
            st.success("Agenda inserida com sucesso")
            time.sleep(2)
            st.rerun()
        
