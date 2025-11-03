import streamlit as st
from views import View

class AvaliarProfissionalUI:
    def main():
        st.header("Avaliar Profissionais")
        id_cliente = st.session_state["usuario_id"]
        profissionais = View.avaliacao_listar_profissionais_para_avaliar(id_cliente)

        if not profissionais:
            st.info("Você já avaliou todos os seus agendamentos finalizados, ou não tem agendamentos para avaliar.")
            return
        
        opcoes = [None] + profissionais

        profissional_selecionado = st.selectbox(
            "Selecione o profissional que deseja avaliar: ",
            options=opcoes,
            index=0, 
            format_func=lambda p: "Selecione um profissonal..." if p is None else f"{p["nome"]} ({p["especialidade"]})"
        )

        if profissional_selecionado:
            id_profissional = profissional_selecionado['id']
            nome_profissional = profissional_selecionado['nome']
            
            st.subheader(f"Avaliar {nome_profissional}")

            form_key = f"avaliacao_form_{id_profissional}"
        
            with st.form(key=form_key):
                nota = st.slider("Nota (0 estrela é péssimo, 5 estrelas é excelente)", 0, 5, 0)
                comentario = st.text_area("Comentário (Opcional):")
                submit_button = st.form_submit_button(label="Enviar Avaliação")
                if submit_button:
                    try:
                        View.avaliacao_inserir(nota, comentario, id_cliente, id_profissional)
                        st.success(f"Avaliação enviada com sucesso para {nome_profissional}!")
                        st.balloons()
                        st.rerun() 
                    except ValueError as e:
                        st.error(f"Erro ao enviar avaliação: {e}")
                    except Exception as e:
                        st.error(f"Ocorreu um erro interno: {e}")