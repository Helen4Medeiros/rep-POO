import streamlit as st
from views import View
import time

class AgendaServicos:
    def main():
        st.header("Agendar Serviços")
        profissionais = View.profissional_listar()
        if len(profissionais) == 0: st.write("Nenhum profissional cadastrado")
        else: 
            profissional = st.selectbox("Informe o profissional", profissionais)
            horarios = View.horario_listar(profissional.get_id())
        
        if len(horarios) == 0: st.write("Nenhum horário disponível")
        else:
            horario = st.selectbox("Informe o horário", horarios)
            servicos = View.servico_listar()
            servico = st.selectbox("Informe o servico", servicos)
            if st.button("Agendar"):
                View.horario_atualizar(horario.get_id(), 
                    horario.get_data(), False, st.session_state["usuario_id"], 
                    servico.get_id(), profissional.get_id())
                
                st.success("Serviço agendado com sucesso")
                time.sleep(2)
                st.rerun()