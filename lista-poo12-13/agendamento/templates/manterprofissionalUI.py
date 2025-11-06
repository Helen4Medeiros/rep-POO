import streamlit as st
import pandas as pd
import time
from views import View

class ManterProfissionalUI: 
    def main(): 
        st.header('Cadastro de Profissional')
        tab1, tab2, tab3, tab4 = st.tabs(['Listar', 'Inserir', 'Atualizar', 'Excluir'])
        with tab1: ManterProfissionalUI.listar()
        with tab2: ManterProfissionalUI.inserir()
        with tab3: ManterProfissionalUI.atualizar()
        with tab4: ManterProfissionalUI.excluir()

    def listar():
        profissional = View.profissional_listar()
        if len(profissional) == 0: st.write('Nenhum profissional cadastrado')
        else: 
            list_dic = []
            for obj in profissional: 
                dados = obj.to_json()
                del dados['senha']
                list_dic.append(dados)
            df = pd.DataFrame(list_dic)
            st.dataframe(df)
    
    def inserir():
        nome = st.text_input('Informe o nome')
        especialidade = st.text_input('Informe o especialidade')
        conselho = st.text_input('Informe o conselho')
        email = st.text_input('Informe o email')
        senha = st.text_input('Informe a senha')
        if st.button("Inserir"):
            try:
                View.profissional_inserir(nome, especialidade, conselho, email, senha)
                st.success("Profissional inserido com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))

    def atualizar():
        profissional = View.profissional_listar()
        if len(profissional) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Atualização de profissional", profissional)
            nome = st.text_input("Novo nome", op.get_nome())
            especialidade = st.text_input("Nova especialidade", op.get_especialidade())
            conselho = st.text_input("Novo conselho", op.get_conselho())
            email = st.text_input('Novo o email')
            senha = st.text_input('Nova a senha')
            if st.button("Atualizar"):
                try:
                    id = op.get_id()
                    View.profissional_atualizar(id, nome, especialidade, conselho, email, senha)
                    st.success("Profissional atualizado com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(str(erro))
    
    def excluir():
        profissional = View.profissional_listar()
        if len([profissional]) == 0: st.write("Nenhum profissional cadastrado")
        else:
            op = st.selectbox("Exclusão de profissionais", profissional)
            if st.button("Excluir"):
                try:
                    id = op.get_id()
                    View.profissional_excluir(id)
                    st.success("Profissional excluído com sucesso")
                    time.sleep(2)
                    st.rerun()
                except ValueError as erro:
                    st.error(str(erro))