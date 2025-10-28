import streamlit as st
from views import View
import time

class AgendaProfissional:
      def main():
        st.header("Abrir Minha Agenda")
        data = st.text_input("Informe a data no formato dd/mm/aaaa")
        hi = st.text_input("Informe o horário inicial no formato HH:MM")
        hf = st.text_input("Informe o horário final no formato HH:MM")
        inter = st.text_input("Informe o intervalo entre os horários (mins)")
        if st.button("Abrir Agenda"):
            View.profissional_agenda(data, hi, hf, int(inter), st.session_state["usuario_id"])
            st.success("Agenda criada com sucesso")
            time.sleep(2)
            st.rerun()