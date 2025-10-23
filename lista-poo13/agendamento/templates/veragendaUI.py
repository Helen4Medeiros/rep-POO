import streamlit as st
from views import View
import pandas as pd # type: ignore

class VerAgenda:
    def main():
        dic = []
        st.header("Minha Agenda")
        horarios = View.horario_listar()
        for obj in horarios:
            cliente = View.cliente_listar_id(obj.get_id_cliente())
            servico = View.servico_listar_id(obj.get_id_servico())
            profissional = View.profissional_listar_id(obj.get_id_profissional())
            if cliente != None: cliente = cliente.get_nome()
            if servico != None: servico = servico.get_descricao()
            if profissional != None: profissional = profissional.get_nome()
            if obj.get_id_profissional() == (st.session_state["usuario_id"]):

                dic.append({"id" : obj.get_id(), "data" : obj.get_data(), "confirmado" : obj.get_confirmado(), "cliente" : cliente, "serviço" : servico, "profissional": profissional})
        
        if dic:
            df = pd.DataFrame(dic)
            st.dataframe(df)
        