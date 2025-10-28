import streamlit as st
from views import View
import time

class PerfilProfissionalUI:
    def main():
        st.header("Meus Dados")
        usuario_id = st.session_state.get("usuario_id")
        if usuario_id is None:
            st.warning("Nenhum usuário logado.")
            return
        
        op = View.profissional_listar_id(st.session_state["usuario_id"])
        if op is None:
            st.error("Profissional não encontrado.")
            return
        
        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
        conselho = st.text_input("Informe o novo conselho", op.get_conselho())
        senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
        if st.button("Atualizar"):
            try:
                id = op.get_id()
                View.profissional_atualizar(id, nome, email, especialidade, conselho, senha)
                st.success("Profissional atualizado com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.error(f"Erro: {e}")
            except Exception as e:
                st.error(f"Ocorreu um erro inesperado: {e}")