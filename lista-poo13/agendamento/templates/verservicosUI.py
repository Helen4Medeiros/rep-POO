import streamlit as st
import pandas as pd
from views import View

class VerServicos:
    def main():
        dic = []
        st.header('Ver Serviços')
        horarios = View.horario_listar()
        for obj in horarios:
            cliente = View.cliente_listar_id(obj.get_id_cliente())
            servico = View.servico_listar_id(obj.get_id_servico())
            profissional = View.profissional_listar_id(obj.get_id_profissional())
            if cliente != None: cliente = cliente.get_nome()
            if servico != None: servico = servico.get_descricao()
            if profissional != None: profissional = profissional.get_nome()
            dic.append({"id" : obj.get_id(), "data" : obj.get_data(), "confirmado" : obj.get_confirmado(), "cliente" : cliente, "serviço" : servico, "profissional": profissional})
        
        if dic:
            df = pd.DataFrame(dic)
            st.dataframe(df)
        elif len(dic) == 0:
            st.write("Nenhum serviço cadastrado no momen")
        