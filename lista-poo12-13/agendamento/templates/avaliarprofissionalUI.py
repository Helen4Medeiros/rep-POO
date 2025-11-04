import streamlit as st #type: ignore 
from views import View

class AvaliarProfissionalUI:
    def main():
        st.header("Avaliar Profissionais")
        
        if "usuario_id" not in st.session_state:
            st.error("Erro: Cliente não logado.")
            return

        id_cliente = st.session_state["usuario_id"]
        profissionais = View.avaliacao_listar_profissionais(id_cliente)
        
        if not profissionais:
            st.info("Você não tem profissionais para avaliação no momento.")
            return

        # como o dicionário deve ser exibido ao usuário
        def formatar_profissional(prof_dict):
            return f"{prof_dict['nome']} ({prof_dict['especialidade']})"

        profissional_selecionado = st.selectbox(
            "Selecione o Profissional para avaliar:",
            options=profissionais, 
            index=0, 
            format_func=formatar_profissional 
        )
        
        id_profissional = profissional_selecionado['id']
        nome_profissional = profissional_selecionado['nome']
        
        st.subheader(f"Avaliar {nome_profissional}")

        form_key = f"avaliacao_form_{id_profissional}" 
        
        with st.form(key=form_key):
            nota = st.slider("Nota (0-5): ", 0, 5, 0) 
            comentario = st.text_area("Comentário (opcional):")

            if st.form_submit_button(label=f"Enviar Avaliação para {nome_profissional}"):
                try:
                    View.avaliacao_inserir(nota, comentario, id_cliente, id_profissional)
                    st.success(f"Avaliação enviada com sucesso para {nome_profissional}! Obrigado.")
                    st.balloons()
                    st.rerun() 
                except ValueError as e:
                    st.error(f"Erro ao enviar avaliação: {e}")
                except Exception as e:
                    st.error(f"Ocorreu um erro interno: {e}")