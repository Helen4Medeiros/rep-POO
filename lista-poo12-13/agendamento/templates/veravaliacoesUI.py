import streamlit as st #type: ignore
import pandas as pd #type: ignore
from views import View

class VerAvaliacoesUI:
    def main():
        st.header("Minhas Avaliações")

        if "usuario_id" not in st.session_state:
            st.error("Acesso negado. Esta página é exclusiva para profissionais.")
        
        id_profissional = st.session_state["usuario_id"]

        media = View.profissional_media_avaliacao(id_profissional)
        st.metric(label="Média de Avaliações", value=f"{media:.1f} / 5.0")

        df_avaliacoes = View.avaliacao_listar_por_profissionais(id_profissional)
            
        if df_avaliacoes.empty:
            st.info("Você ainda não recebeu nenhuma avaliação.")
        else:
            st.subheader(f"Detalhes das {len(df_avaliacoes)} Avaliações:")
                
            st.dataframe(
                df_avaliacoes,
                use_container_width=True, 
                column_config={
                    "Nota": st.column_config.NumberColumn(
                        "Nota",
                        format="%d / 5",
                        help="Nota dada pelo cliente"
                    )
                },
            )    