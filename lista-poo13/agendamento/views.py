from models.servico import Servico, ServicoDAO
from models.cliente import Cliente, ClienteDAO
from models.horario import Horario, HorarioDAO
from models.profissional import Profissional, ProfissionalDAO
from datetime import datetime as dt
from datetime import timedelta

class View:
        
    # cliente
    def cliente_listar():
        return ClienteDAO.listar()
    def cliente_listar_objetos():
        return ClienteDAO.listar_clientes()
    def cliente_inserir(nome, email, fone, senha):
        if not nome:
            raise ValueError("O nome do cliente é obrigatório.")
        if not email:
            raise ValueError("O e-mail do cliente é obrigatório.")
        if not senha:
            raise ValueError("A senha do cliente é obrigatória.")

        if email.strip().lower() == "admin":
            raise ValueError("O e-mail 'admin' é reservado ao administrador.")
        
        for c in ClienteDAO.listar():
            if c.get_email().strip().lower() == email.strip().lower() and c.get_id() != id:
                raise ValueError("Já existe outro cliente com esse e-mail.")
            
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)
    def cliente_atualizar(id, nome, email, fone, senha):
        email = email.strip().lower()
        if email == "admin":
            raise ValueError("O email 'admin' é reservado ao administrador.")
        
        for c in ClienteDAO.listar():
            if c.get_email() == email:
                raise ValueError("Já existe um cliente com esse email.")
            
        for p in ProfissionalDAO.listar():
            if p.get_email() == email:
                raise ValueError('Já existe um profissional com esse email.')

        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)
    def cliente_excluir(id):
        for h in HorarioDAO.listar():
            if h.get_id_cliente() == id:
                raise ValueError("Não é possível excluir um cliente com horários agendados.")
        cliente = Cliente(id, "", "", "", "")
        ClienteDAO.excluir(cliente)
    def cliente_listar_id(id):
        cliente = ClienteDAO.listar_id(id)
        return cliente
    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return
        View.cliente_inserir("admin", "admin", "fone", "1234")
    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return {"id" : c.get_id(), "nome" : c.get_nome()}
        return None

    # servico
    def servico_listar():
        return ServicoDAO.listar()
    def servico_inserir(descricao, valor):
        servico = Servico(0, descricao, valor)
        ServicoDAO.inserir(servico)
    def servico_atualizar(id, descricao, valor):
        servico = Servico(id, descricao, valor)
        ServicoDAO.atualizar(servico)
    def servico_excluir(id):
        servico = Servico(id, "", "")
        ServicoDAO.excluir(servico)
    def servico_listar_id(id):
        servico = ServicoDAO.listar_id(id)
        return servico

    # horario
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO.inserir(c)
    def horario_listar():
        return HorarioDAO.listar()
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_cliente(id_cliente)
        c.set_id_servico(id_servico)
        c.set_id_profissional(id_profissional)
        HorarioDAO.atualizar(c)
    def horario_excluir(id):
        c = Horario(id, None)
        HorarioDAO.excluir(c)
    
    def horario_agendar_horario(id_profissional):
        r = []
        agora = dt.now()
        for h in View.horario_listar():
            if h.get_data() > agora and h.get_confirmado() == False and h.get_id_cliente() == 0 and h.get_id_profissional() == id_profissional:
                r.append(h)
        r.sort(key = lambda h: h.get_data())
        return r

    # profissional
    def profissional_listar():
        return ProfissionalDAO.listar()
    def profissional_listar_profissionais():
        return ProfissionalDAO.listar_profissionais()
    def profissional_inserir(nome, especialidade, conselho, email, senha):
        if not nome.strip():
            raise ValueError("O nome do profissional é obrigatório.")
        if not email.strip():
            raise ValueError("O e-mail do profissional é obrigatório.")
        if not senha.strip():
            raise ValueError("A senha do profissional é obrigatória.")
        if email.strip().lower() == "admin":
            raise ValueError("O e-mail 'admin' é reservado ao administrador.")
    
        for c in View.cliente_listar():  
            if c.get_email().strip().lower() == email.strip().lower():
                raise ValueError("Já existe um cliente com este e-mail.")
        for p in ProfissionalDAO.listar():  
            if p.get_email().strip().lower() == email.strip().lower():
                raise ValueError("Já existe um profissional com este e-mail.")
        
        profissional = Profissional(0, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.inserir(profissional)
    def profissional_atualizar(id, nome, especialidade, conselho, email, senha):
        if not nome.strip():
            raise ValueError("O nome do profissional é obrigatório.")
        if not email.strip():
            raise ValueError("O e-mail do profissional é obrigatório.")
        if not senha.strip():
            raise ValueError("A senha do profissional é obrigatória.")
        if email.strip().lower() == "admin":
            raise ValueError("O e-mail 'admin' é reservado ao administrador.")
    
        for c in View.cliente_listar():  
            if c.get_email().strip().lower() == email.strip().lower():
                raise ValueError("Já existe um cliente com este e-mail.")
        for p in ProfissionalDAO.listar():  
            if p.get_email().strip().lower() == email.strip().lower():
                raise ValueError("Já existe um profissional com este e-mail.")

        profissional = Profissional(id, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.atualizar(profissional)
    def profissional_excluir(id):
        for h in HorarioDAO.listar():
            if h.get_id_profissional() == id:
                raise ValueError("Não é possível excluir um profissional com horários agendados.")
        profissional = Profissional(id, "", "", "", "", "")
        ProfissionalDAO.excluir(profissional)
    def profissional_listar_id(id):
        profissional = ProfissionalDAO.listar_id(id)
        return profissional
    def profissional_autenticar(email, senha):
        for p in View.profissional_listar():
            if p.get_email() == email and p.get_senha() == senha:
                return {"id" : p.get_id(), "nome" : p.get_nome()}
    def profissional_agenda(data, inicio, fim, int, id):
        h_primeiro = dt.strptime(data + " " + inicio, "%d/%m/%Y %H:%M")
        h_ultimo = dt.strptime(data + " " + fim, "%d/%m/%Y %H:%M")
        int_min = timedelta(minutes = int)
        x = h_primeiro
        while x <= h_ultimo:
            View.horario_inserir(x, False, None, None, id)
            x += int_min

    @staticmethod
    def horarios_confirmar(id_profissional):
        dic = []
        for h in HorarioDAO.listar():
            if (
                h.get_id_profissional() == id_profissional and 
                not h.get_confirmado() and 
                h.get_id_cliente() != None
            ):
                cliente = ClienteDAO.listar_id(h.get_id_cliente())
                servico = ServicoDAO.listar_id(h.get_id_servico())
                dic.append({
                    "id": h.get_id(),
                    "data": h.get_data().strftime("%d/%m/%Y %H:%M"),
                    "cliente": cliente.get_nome() if cliente else None,
                    "servico": servico.get_descricao() if servico else None
                })
        return dic
    
    @staticmethod
    def confirmar_horario(id_horario):
        h = HorarioDAO.listar_id(id_horario)
        if not h:
            return False
        h.set_confirmado(True)
        HorarioDAO.atualizar(h)
        return True


