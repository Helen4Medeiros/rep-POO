from templates.manterservicoUI import ManterServicoUI
from templates.manterclienteUI import ManterClienteUI
from templates.manterhorarioUI import ManterHorarioUI
from templates.manterprofissionalUI import ManterProfissionalUI
from templates.abrircontaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.perfilclienteUI import PerfilClienteUI
from templates.perfilprofissionalUI import PerfilProfissionalUI
from templates.agendaprofissionalUI import AgendaProfissional
from templates.agendaservicosUI import AgendaServicosUI
from templates.avaliarprofissionalUI import AvaliarProfissionalUI
from templates.veragendaUI import VerAgenda
from templates.verservicosUI import VerServicos
from templates.confirmarservicosUI import ConfirmarServicos
from views import View
import streamlit as st

class IndexUI:
    def menu_admin():            
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais"])
        if op == "Cadastro de Clientes": ManterClienteUI.main()
        if op == "Cadastro de Serviços": ManterServicoUI.main()
        if op == "Cadastro de Horários": ManterHorarioUI.main()
        if op == "Cadastro de Profissionais": ManterProfissionalUI.main()

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Abrir Conta"])
        if op == "Entrar no Sistema": LoginUI.main()
        if op == "Abrir Conta": AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Visualizar Serviços", "Agendar Serviços", "Avaliar Profissionais"])
        if op == "Meus Dados": PerfilClienteUI.main()
        if op == "Visualizar Serviços": VerServicos.main()
        if op == "Agendar Serviços": AgendaServicosUI.main()
        if op == "Avaliar Profissionais": AvaliarProfissionalUI.main()

    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Minha Agenda", "Abrir Agenda", "Confirmar Serviço"])
        if op == "Meus Dados": PerfilProfissionalUI.main()
        if op == "Minha Agenda": VerAgenda.main()
        if op == "Abrir Agenda": AgendaProfissional.main()
        if op == 'Confirmar Serviço': ConfirmarServicos.main()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            cliente = st.session_state["usuario_tipo"] == "cliente" 
            profissional = st.session_state["usuario_tipo"] == "profissional" 
            admin = st.session_state["usuario_nome"] == "admin"
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin: IndexUI.menu_admin()
            elif cliente: IndexUI.menu_cliente() 
            elif profissional: IndexUI.menu_profissional() 
            IndexUI.sair_do_sistema()

    def main():
        View.cliente_criar_admin() 
        IndexUI.sidebar() 

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()
IndexUI.main()