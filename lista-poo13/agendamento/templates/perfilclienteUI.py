import streamlit as st
from views import View
import time

class PerfilClienteUI:
    def main():
        st.header("Meus Dados")
        usuario_id = st.session_state.get("usuario_id")
        if usuario_id is None:
            st.warning("Nenhum usuário logado.")
            return
        
        cliente = View.cliente_listar_id(usuario_id)
        if cliente is None:
            st.error("Cliente não encontrado.")
            return
        
        nome = st.text_input("Informe o novo nome", cliente.get_nome())
        email = st.text_input("Informe o novo e-mail", cliente.get_email())
        fone = st.text_input("Informe o novo fone", cliente.get_fone())
        senha = st.text_input("Informe a nova senha", cliente.get_senha(),
        type="password")

        if st.button("Atualizar"):
            try:
                id = op.get_id()
                View.cliente_atualizar(id, nome, email, fone, senha)
                st.success("Cliente atualizado com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as e:
                st.error(f"Erro: {e}")
            except Exception as e:
                st.error(f"Ocorreu um erro inesperado: {e}")

