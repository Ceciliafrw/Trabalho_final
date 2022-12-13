from cgitb import text
from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as lite
from typing_extensions import Self
from view import *
from banco import *

####################### cores ############################
co0 = "#f0f3f5" #Preto
c01 = "#feffff" #Branca
c02 = "#4fa882" #verde
c03 = "#38576b" #valor
c04 = "#403d3d" #branca
c05 = "#e06636" #laranja
c06 = "#038cfc" #azul
c07 = "#ff0000" #vermelho
c08 = "#263238" #cinza
c09 = "#e9edf5" #cinza claro
##########################################################
janela = Tk()
####### criando conexao com banco de dados ##########
conexao = lite.connect('dados.db')
##########################################################
   
class tela:
    def __init__(self):
        self.janela = janela
        self.tela()
        self.frame_tela()
        self.botoes_padroes()
        banco_dados()

        janela.mainloop()

    def tela(self):
        self.janela.title("Agendador")
        self.janela.configure(background=c09)
        self.janela.geometry("1043x453")
        self.janela.resizable(True, True)
        self.janela.maxsize(width=1250, height=650)
        self.janela.minsize(width=750, height=350)

    def frame_tela(self):
        ################### dividindo a janela ###################
#################### formatando tela a direita para cadastro Usuario ###################
        self.frame_cima = Frame(self.janela, bd=4, width=310, height=50, bg=c02, relief='flat') ### faixa_cadastro
        self.frame_cima.grid(row=0, column=0) ###frame.cima

        self.frame_baixo = Frame(self.janela,bd=4, width=310, height=403, bg=c01, relief='flat') ### tela_cadastro
        self.frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1) ###frame.baixo

################ formatando tela a esquerda para apresentar a Tabela  ###############
        self.frame_direita= Frame(self.janela,bd=4, width=588, height=403, bg=c01, relief='flat') ### tela_apresenta
        self.frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW) ###frame.direita

    def botoes_padroes(self):
        ####### botao usuario #######
        self.b_usuario = Button(self.frame_baixo,command=usuario, text='Usuario', width =10, font=('Ivy 9 bold'),bg=c03,fg=c01,bd=3, relief='raised', overrelief='ridge')
        self.b_usuario.place(x=7, y=350)

        self.b_evento = Button(self.frame_baixo,command=evento, text='Evento', width =10, font=('Ivy 9 bold'),bg=c06,fg=c01,bd=3, relief='raised', overrelief='ridge')
        self.b_evento.place(x=107, y=350)

        self.b_agendar = Button(self.frame_baixo, text='Agendar',  width =10, font=('Ivy 9 bold'),bg=c02,fg=c01,bd=3, relief='raised', overrelief='ridge')
        self.b_agendar.place(x=207, y=350)

class usuario():
    global tree

    def __init__(self):
        self.janela = janela
        self.tela_usuario()
        self.formulario_usuario()
        mostra_tabela_usuario()
        
        janela.mainloop()

    def conexao_tela_usuario(self):
        c = tela()
        self.janela_u = janela
        self.conexao_u = conexao
       
    def tela_usuario(self):
        ############### Inserindo formulario de Usuario ###############
        self.titulo_u = Label(janela, text='Formulário',anchor=NW, font=('Ivy 13 bold'), bg=c02,fg=c01, relief='flat')
        self.titulo_u.place(x=10, y=10)  

        self.b_inserir = Button(janela,command=self.inserir_usuario_tabela, text='Inserir',width =10, font=('Ivy 9 bold'), bg=c09,fg=c08,bd=3, relief='raised', overrelief='ridge')
        self.b_inserir.place(x=10, y=310)

        self.b_atualizar = Button(janela,command=self.atualizar_tabela, text='Atualizar', width =10, font=('Ivy 9 bold'),bg=c09,fg=c08,bd=3, relief='raised', overrelief='ridge')
        self.b_atualizar.place(x=110, y=310)

        self.b_deletar = Button(janela,command=self.deletar_tabela, text='Deletar', width =10, font=('Ivy 9 bold'),bg=c09,fg=c08,bd=3, relief='raised', overrelief='ridge')
        self.b_deletar.place(x=210, y=310)

        self.b_limpar = Button(janela,command=self.limpar_tela, text='Limpar', width =10, font=('Ivy 9 bold'),bg=c09,fg=c08,bd=3, relief='raised', overrelief='ridge')
        self.b_limpar.place(x=10, y=350)

        self.b_voltar = Button(janela,command=tela, text='Voltar', width =10, font=('Ivy 9 bold'),bg=c09,fg=c08,bd=3, relief='raised', overrelief='ridge')
        self.b_voltar.place(x=110, y=350)

        self.b_exportar = Button(janela, text='Exportar', width =10, font=('Ivy 9 bold'),bg=c09,fg=c08,bd=3, relief='raised', overrelief='ridge')
        self.b_exportar.place(x=210, y=350)
 
    def formulario_usuario(self):  
        self.l_nome = Label(janela, text='Nome*', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_nome.place(x=10, y=50)
        self.e_nome = Entry(janela , width =48, justify='left',relief='solid')
        self.e_nome.place(x=15, y=70)

        self.l_logra = Label(janela, text='Logradouro', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_logra.place(x=10, y=90)
        self.e_logra = Entry(janela, width =40, justify='left',relief='solid')
        self.e_logra.place(x=15, y=110)

        self.l_num = Label(janela, text='Nº', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_num.place(x=266, y=90)
        self.e_num = Entry(janela, width =5, justify='left',relief='solid')
        self.e_num.place(x=272, y=110)

        self.l_bairro = Label(janela, text='Bairro', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_bairro.place(x=10, y=130)
        self.e_bairro = Entry(janela, width =30,justify='left',relief='solid')
        self.e_bairro.place(x=15, y=150)

        self.l_cep = Label(janela, text='CEP', anchor=NW, font=('Ivy 10 bold'),bg=c01,fg=c04, relief='flat')
        self.l_cep.place(x=210, y=130)
        self.e_cep = Entry(janela, width =14,justify='left',relief='solid')
        self.e_cep.place(x=216, y=150)

        self.l_cid = Label(janela, text='Cidade', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_cid.place(x=10, y=170)
        self.e_cid = Entry(janela, width =22,justify='left',relief='solid')
        self.e_cid.place(x=15, y=190)

        self.l_estado = Label(janela, text='Estado', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_estado.place(x=158, y=170)
        self.e_estado = Entry(janela, width =5,justify='left',relief='solid')
        self.e_estado.place(x=168, y=190)

        self.l_idade = Label(janela, text='Idade', anchor=NW, font=('Ivy 10 bold'),bg=c01,fg=c04, relief='flat')
        self.l_idade.place(x=219, y=170)
        self.e_idade = Entry(janela, width =5,justify='left',relief='solid')
        self.e_idade.place(x=220, y=190)

        self.l_gen = Label(janela, text='Genêro', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_gen.place(x=258, y=170)
        self.e_gen = Entry(janela, width =5, justify='left',relief='solid')
        self.e_gen.place(x=270, y=190)
            
        self.l_tel = Label(janela, text='Telefone', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_tel.place(x=10, y=210)
        self.e_tel = Entry(janela, width =22, justify='left',relief='solid')
        self.e_tel.place(x=15, y=230)

        self.l_cpf = Label(janela, text='CPF', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_cpf.place(x=160, y=210)
        self.e_cpf = Entry(janela, width =22, justify='left',relief='solid')
        self.e_cpf.place(x=170, y=230)
                    
        self.l_email = Label(janela, text='Email*', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_email.place(x=10, y=250)
        self.e_email = Entry(janela, width =48, justify='left',relief='solid')
        self.e_email.place(x=15, y=270)

    def limpar_tela(self):
        self.e_nome.delete(0, 'end')
        self.e_logra.delete(0, 'end')
        self.e_num.delete(0, 'end')
        self.e_bairro.delete(0, 'end')
        self.e_cep.delete(0, 'end')
        self.e_cid.delete(0, 'end')
        self.e_estado.delete(0, 'end')
        self.e_idade.delete(0, 'end')
        self.e_gen.delete(0, 'end')
        self.e_tel.delete(0, 'end')
        self.e_cpf.delete(0, 'end')
        self.e_email.delete(0, 'end')
   
    def inserir_usuario_tabela(self):
    ##### atualizar tabela #####
        nome = self.e_nome.get()
        logradouro= self.e_logra.get()
        num= self.e_num.get()
        bairro = self.e_bairro.get()
        cep = self.e_cep.get()
        cidade = self.e_cid.get()
        estado = self.e_estado.get()
        idade= self.e_idade.get()
        genero= self.e_gen.get()
        telefone= self.e_tel.get()
        cpf= self.e_cpf.get()
        email = self.e_email.get()
        
        lista = [nome, logradouro, num, bairro, cep, cidade, estado, idade, genero, telefone, cpf, email]

        if nome =='':
            messagebox.showerror('Erro', 'O nome não pode ser vario!')
        else:
            inserir_info(lista)    
            messagebox.showerror('Sucesso', "Os dados foram inseridos com sucesso!")

            nome = self.e_nome.delete(0, 'end')
            logradouro= self.e_logra.delete(0, 'end')
            num= self.e_num.delete(0, 'end')
            bairro = self.e_bairro.delete(0, 'end')
            cep = self.e_cep.delete(0, 'end')
            cidade = self.e_cid.delete(0, 'end')
            estado = self.e_estado.delete(0, 'end')
            idade= self.e_idade.delete(0, 'end')
            genero= self.e_gen.delete(0, 'end')
            telefone= self.e_tel.delete(0, 'end')
            cpf= self.e_cpf.delete(0, 'end')
            email = self.e_email.delete(0, 'end')

                            
            #for widget in mostra_tabela_usuario().winfo_children():
                #widget.destroy()
            
            mostra_tabela_usuario()

    def atualizar_tabela(self):
        try:
            treev_dados = self.tree.focus()
            treev_dicionario = self.tree.item(treev_dados)
            tree_lista = treev_dicionario['values']

            valor_id = tree_lista[0]

            self.e_nome.delete(0, 'end')
            self.e_logra.delete(0, 'end')
            self.e_num.delete(0, 'end')
            self.e_bairro.delete(0, 'end')
            self.e_cep.delete(0, 'end')
            self.e_cid.delete(0, 'end')
            self.e_estado.delete(0, 'end')
            self.e_idade.delete(0, 'end')
            self.e_gen.delete(0, 'end')
            self.e_tel.delete(0, 'end')
            self.e_cpf.delete(0, 'end')
            self.e_email.delete(0, 'end')
                
            self.e_nome.insert(0, tree_lista[1])
            self.e_logra.insert(0, tree_lista[2])
            self.e_num.insert(0, tree_lista[3])
            self.e_bairro.insert(0, tree_lista[4])
            self.e_cep.insert(0, tree_lista[5])
            self.e_cid.insert(0, tree_lista[6])
            self.e_estado.insert(0, tree_lista[7])
            self.e_idade.insert(0, tree_lista[8])
            self.e_gen.insert(0, tree_lista[9])
            self.e_tel.insert(0, tree_lista[10])
            self.e_cpf.insert(0, tree_lista[11])
            self.e_email.insert(0, tree_lista[12])
            
            def update():    
                nome = self.e_nome.delete(0, 'end')
                logradouro = self.e_logra.delete(0, 'end')
                num = self.e_num.delete(0, 'end')
                bairro = self.e_bairro.delete(0, 'end')
                cep = self.e_cep.delete(0, 'end')
                cidade = self.e_cid.delete(0, 'end')
                estado = self. e_estado.delete(0, 'end')
                idade = self.e_idade.delete(0, 'end')
                genero = self.e_gen.delete(0, 'end')
                telefone = self.e_tel.delete(0, 'end')
                cpf = self.e_cpf.delete(0, 'end')
                email = self.e_email.delete(0, 'end')
                
                lista = [valor_id,nome, logradouro, num, bairro, cep, cidade, estado, idade, genero, telefone, cpf, email]

                if nome or logradouro or num or bairro or cep or cidade or estado or idade or genero or telefone or cpf or email == '':
                    messagebox.showerror('Erro', 'Nenhum campo não pode ser vario!')

                elif cpf == cpf:
                    messagebox.showerror('Erro', 'CPF é unico por usuário!')

                else:
                    atualizar_info(lista)
                    messagebox.showerror('Sucesso', "Os dados foram atualizados com sucesso!")

                    self.e_nome.delete(0, 'end')
                    self.e_logra.delete(0, 'end')
                    self.e_num.delete(0, 'end')
                    self.e_bairro.delete(0, 'end')
                    self.e_cep.delete(0, 'end')
                    self.e_cid.delete(0, 'end')
                    self.e_estado.delete(0, 'end')
                    self.e_idade.delete(0, 'end')
                    self.e_gen.delete(0, 'end')
                    self.e_tel.delete(0, 'end')
                    self.e_cpf.delete(0, 'end')
                    self.e_email.delete(0, 'end')
                    
                for widget in mostra_tabela_usuario.winfo_children():
                    widget.destroy()

                mostra_tabela_usuario()
                    
        #### Botao para atualizar  ####
            
        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

    def deletar_tabela(self):
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            tree_lista = treev_dicionario['values']

            valor_id = [tree_lista[0]]

            deletar_info(valor_id)
            messagebox.showerror('Sucesso', "Os dados foram deletados da tabela com sucesso!")

            #for widget in mostra_tabela_usuario().winfo_children():
                #widget.destroy()
                
            mostra_tabela_usuario()

        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

        mostra_tabela_usuario()

def mostra_tabela_usuario():
    global tree
    ################ formatando tela a esquerda para apresentar a Tabela  ###############
    frame_direita= Frame(janela,bd=4, width=588, height=403, bg=c01, relief='flat') ### tela_apresenta
    frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW) ###frame.direita
    #********criando o visual da tabela a direita*******
    
        #Inserindo formulario de Usuario
    cabecalho = ['ID','NOME COMPLETO','LOGRADOURO','Nº','BAIRRO','CIDADE','EST','CEP','IDADE','TELEFONE','CPF','GEN','E-MAIL']
       
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=cabecalho, show="headings")

            #*********criando a barra de rolagem vertical*********
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

            #*********criando a barra de rolagem horizontal*********
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

            #*********ativando a barra de rolagem*********
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

            #*********posicionando a barra de rolagem*********
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frame_direita.grid_rowconfigure(0,weight=12)

            #*****configurando as colunas da tabela
    hd=["nw","nw","nw","nw","nw","nw","nw","nw","nw","nw","nw","center","center"]
    h=[20,150,150,30,100,100,50,100,30,100,100,50,100]
    n=0

    for coluna in cabecalho:
        tree.heading(coluna, text=coluna.title(),anchor=CENTER)
        tree.column(coluna,width=h[n],anchor=hd[n])
        n+=1

    lista = mostrar_info()
    for item in lista:
        tree.insert('', 'end', values=item)
 
class evento():
    global tree

    def __init__(self):
        self.janela = janela
        self.tela_evento()
        self.formulario_evento()
        mostra_tabela_evento()
        
        janela.mainloop()

    def conexao_tela_evento(self):
        c = tela()
        self.janela_u = janela
        self.conexao_u = conexao
       
    def tela_evento(self):
        ############### Inserindo formulario de Usuario ###############
        self.titulo_u = Label(janela, text='Evento',anchor=NW, font=('Ivy 13 bold'), bg=c02,fg=c01, relief='flat')
        self.titulo_u.place(x=10, y=10)  

        self.b_inserir = Button(janela,command=self.inserir_evento_tabela, text='Inserir',width =10, font=('Ivy 9 bold'), bg=c09,fg=c08,bd=3, relief='raised', overrelief='ridge')
        self.b_inserir.place(x=10, y=310)

        self.b_atualizar = Button(janela,command=self.atualizar_tabela_evento, text='Atualizar', width =10, font=('Ivy 9 bold'),bg=c09,fg=c08,bd=3, relief='raised', overrelief='ridge')
        self.b_atualizar.place(x=110, y=310)

        self.b_deletar = Button(janela,command=self.deletar_tabela_evento, text='Deletar', width =10, font=('Ivy 9 bold'),bg=c09,fg=c08,bd=3, relief='raised', overrelief='ridge')
        self.b_deletar.place(x=210, y=310)

        self.b_limpar = Button(janela,command=self.limpar_tela_evento, text='Limpar', width =10, font=('Ivy 9 bold'),bg=c09,fg=c08,bd=3, relief='raised', overrelief='ridge')
        self.b_limpar.place(x=10, y=350)

        self.b_voltar = Button(janela,command=tela, text='Voltar', width =10, font=('Ivy 9 bold'),bg=c09,fg=c08,bd=3, relief='raised', overrelief='ridge')
        self.b_voltar.place(x=110, y=350)

        self.b_exportar = Button(janela, text='Exportar', width =10, font=('Ivy 9 bold'),bg=c09,fg=c08,bd=3, relief='raised', overrelief='ridge')
        self.b_exportar.place(x=210, y=350)
 
    def formulario_evento(self):  
        self.l_evento = Label(janela, text='Evento*', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_evento.place(x=10, y=50)
        self.e_evento = Entry(janela , width =48, justify='left',relief='solid')
        self.e_evento.place(x=15, y=70)

        self.l_data = Label(janela, text='Data*', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_data.place(x=10, y=90)
        self.e_data = Entry(janela, width =40, justify='left',relief='solid')
        self.e_data.place(x=15, y=110)

        self.l_cid = Label(janela, text='Cidade*', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_cid.place(x=10, y=170)
        self.e_cid = Entry(janela, width =22,justify='left',relief='solid')
        self.e_cid.place(x=15, y=190)

        self.l_estado = Label(janela, text='Estado*', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_estado.place(x=158, y=170)
        self.e_estado = Entry(janela, width =5,justify='left',relief='solid')
        self.e_estado.place(x=168, y=190)

        self.l_local = Label(janela, text='Local*', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_local.place(x=10, y=130)
        self.e_local = Entry(janela, width =30,justify='left',relief='solid')
        self.e_local.place(x=15, y=150)

        self.l_espaco = Label(janela, text='Espaço*', anchor=NW, font=('Ivy 10 bold'),bg=c01,fg=c04, relief='flat')
        self.l_espaco.place(x=210, y=130)
        self.e_espaco = Entry(janela, width =14,justify='left',relief='solid')
        self.e_espaco.place(x=216, y=150)

        self.l_tipo = Label(janela, text='Tipo*', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_tipo.place(x=266, y=90)
        self.e_tipo = Entry(janela, width =5, justify='left',relief='solid')
        self.e_tipo.place(x=272, y=110)

        self.l_valor = Label(janela, text='Valor Ingresso*', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_valor.place(x=258, y=170)
        self.e_valor = Entry(janela, width =5, justify='left',relief='solid')
        self.e_valor.place(x=270, y=190)
            
        self.l_descricao = Label(janela, text='Descrição*', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_descricao.place(x=10, y=250)
        self.e_descricao = Entry(janela, width =48, justify='left',relief='solid')
        self.e_descricao.place(x=15, y=270)

    def limpar_tela_evento(self):
        self.e_evento.delete(0, 'end')
        self.e_data.delete(0, 'end')
        self.e_cid.delete(0, 'end')
        self.e_estado.delete(0, 'end')
        self.e_local.delete(0, 'end')
        self.e_espaco.delete(0, 'end')
        self.e_tipo.delete(0, 'end')
        self.e_valor.delete(0, 'end')
        self.e_descricao.delete(0, 'end')
   
    def inserir_evento_tabela(self):
    ##### atualizar tabela #####
        evento = self.e_evento.get()
        data= self.e_data.get()
        cidade = self.e_cid.get()
        estado = self.e_estado.get()
        local = self.e_local.get()
        espaco = self.e_espaco.get()
        tipo = self.e_tipo.get()
        valor = self.e_valor.get()
        descricao = self.e_descricao.get()
        
        lista = [evento, data, cidade, estado, local, espaco, tipo, valor, descricao]

        if evento =='':
            messagebox.showerror('Erro', 'O nome não pode ser vario!')
        else:
            inserir_info(lista)    
            messagebox.showerror('Sucesso', "Os dados foram inseridos com sucesso!")

            self.e_evento.delete(0, 'end')
            self.e_data.delete(0, 'end')
            self.e_cid.delete(0, 'end')
            self.e_estado.delete(0, 'end')
            self.e_local.delete(0, 'end')
            self.e_espaco.delete(0, 'end')
            self.e_tipo.delete(0, 'end')
            self.e_valor.delete(0, 'end')
            self.e_descricao.delete(0, 'end')

                            
            #for widget in mostra_tabela_usuario().winfo_children():
                #widget.destroy()
            
            mostra_tabela_evento()

    def atualizar_tabela_evento(self):
        try:
            treev_dados = self.tree.focus()
            treev_dicionario = self.tree.item(treev_dados)
            tree_lista = treev_dicionario['values']

            valor_id = tree_lista[0]

            self.e_evento.delete(0, 'end')
            self.e_data.delete(0, 'end')
            self.e_cid.delete(0, 'end')
            self.e_estado.delete(0, 'end')
            self.e_local.delete(0, 'end')
            self.e_espaco.delete(0, 'end')
            self.e_tipo.delete(0, 'end')
            self.e_valor.delete(0, 'end')
            self.e_descricao.delete(0, 'end')
                
            self.e_evento.insert(0, tree_lista[1])
            self.e_data.insert(0, tree_lista[2])
            self.e_cid.insert(0, tree_lista[3])
            self.e_estado.insert(0, tree_lista[4])
            self.e_local.insert(0, tree_lista[5])
            self.e_espaco.insert(0, tree_lista[6])
            self.e_tipo.insert(0, tree_lista[7])
            self.e_valor.insert(0, tree_lista[8])
            self.e_descricao.insert(0, tree_lista[9])
            
            def update():    
                evento = self.e_evento.delete(0, 'end')
                data= self.e_data.delete(0, 'end')
                cidade = self.e_cid.delete(0, 'end')
                estado = self.e_estado.delete(0, 'end')
                local = self.e_local.delete(0, 'end')
                espaco = self.e_espaco.delete(0, 'end')
                tipo = self.e_tipo.delete(0, 'end')
                valor = self.e_valor.delete(0, 'end')
                descricao = self.e_descricao.delete(0, 'end')
                
                lista = [valor_id,evento, data, cidade, estado, local, espaco, tipo, valor, descricao]
                #or logradouro or num or bairro or cep or cidade or estado or idade or genero or telefone or cpf or email
                if evento  == '':
                    messagebox.showerror('Erro', 'Nenhum campo não pode ser vario!')

                #elif cpf == cpf:
                    #messagebox.showerror('Erro', 'CPF é unico por usuário!')

                else:
                    atualizar_info_evento(lista)
                    messagebox.showerror('Sucesso', "Os dados foram atualizados com sucesso!")

                    evento = self.e_evento.delete(0, 'end')
                    data= self.e_data.delete(0, 'end')
                    cidade = self.e_cid.delete(0, 'end')
                    estado = self.e_estado.delete(0, 'end')
                    local = self.e_local.delete(0, 'end')
                    espaco = self.e_espaco.delete(0, 'end')
                    tipo = self.e_tipo.delete(0, 'end')
                    valor = self.e_valor.delete(0, 'end')
                    descricao = self.e_descricao.delete(0, 'end')
                #for widget in mostra_tabela_usuario.winfo_children():
                    #widget.destroy()

                mostra_tabela_evento()
                    
        #### Botao para atualizar  ####
            
        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

    def deletar_tabela_evento(self):
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            tree_lista = treev_dicionario['values']

            valor_id = [tree_lista[0]]

            deletar_info_evento(valor_id)
            messagebox.showerror('Sucesso', "Os dados foram deletados da tabela com sucesso!")

            #for widget in mostra_tabela_usuario().winfo_children():
                #widget.destroy()
                
            mostra_tabela_evento()

        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

        mostra_tabela_evento()

def mostra_tabela_evento():
    global tree
    ################ formatando tela a esquerda para apresentar a Tabela  ###############
    frame_direita= Frame(janela,bd=4, width=588, height=403, bg=c01, relief='flat') ### tela_apresenta
    frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW) ###frame.direita
    #********criando o visual da tabela a direita*******
    
        #Inserindo formulario de _evento
    cabecalho = ['ID','EVENTO','DATA','CIDADE','ESTADO','LOCAL','ESPAÇO','TIPO','VALOR INGRESSO','DESCRIÇÃO']
       
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=cabecalho, show="headings")

            #*********criando a barra de rolagem vertical*********
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

            #*********criando a barra de rolagem horizontal*********
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

            #*********ativando a barra de rolagem*********
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

            #*********posicionando a barra de rolagem*********
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=3, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frame_direita.grid_rowconfigure(0,weight=12)

            #*****configurando as colunas da tabela
    hd=["nw","nw","nw","nw","nw","nw","nw","nw","nw","nw"]
    h=[20,150,150,100,100,100,100,100,100,100]
    n=0

    for coluna in cabecalho:
        tree.heading(coluna, text=coluna.title(),anchor=CENTER)
        tree.column(coluna,width=h[n],anchor=hd[n])
        n+=1

    lista = mostrar_info_evento()
    for item in lista:
        tree.insert('', 'end', values=item)
 
 
class agenda():
    global tree

    def __init__(self):
        self.janela = janela
        self.tela_evento()
        self.formulario_evento()
        mostra_tabela_evento()
        
        janela.mainloop()

    def conexao_tela_evento(self):
        c = tela()
        self.janela_u = janela
        self.conexao_u = conexao
       
    def tela_evento(self):
        ############### Inserindo formulario de Usuario ###############
        self.titulo_u = Label(janela, text='Evento',anchor=NW, font=('Ivy 13 bold'), bg=c02,fg=c01, relief='flat')
        self.titulo_u.place(x=10, y=10)  

        self.b_inserir = Button(janela,command=self.inserir_evento_tabela, text='Inserir',width =10, font=('Ivy 9 bold'), bg=c09,fg=c08,bd=3, relief='raised', overrelief='ridge')
        self.b_inserir.place(x=10, y=310)

        self.b_atualizar = Button(janela,command=self.atualizar_tabela_evento, text='Atualizar', width =10, font=('Ivy 9 bold'),bg=c09,fg=c08,bd=3, relief='raised', overrelief='ridge')
        self.b_atualizar.place(x=110, y=310)

        self.b_deletar = Button(janela,command=self.deletar_tabela_evento, text='Deletar', width =10, font=('Ivy 9 bold'),bg=c09,fg=c08,bd=3, relief='raised', overrelief='ridge')
        self.b_deletar.place(x=210, y=310)

        self.b_limpar = Button(janela,command=self.limpar_tela_evento, text='Limpar', width =10, font=('Ivy 9 bold'),bg=c09,fg=c08,bd=3, relief='raised', overrelief='ridge')
        self.b_limpar.place(x=10, y=350)

        self.b_voltar = Button(janela,command=tela, text='Voltar', width =10, font=('Ivy 9 bold'),bg=c09,fg=c08,bd=3, relief='raised', overrelief='ridge')
        self.b_voltar.place(x=110, y=350)

        self.b_exportar = Button(janela, text='Exportar', width =10, font=('Ivy 9 bold'),bg=c09,fg=c08,bd=3, relief='raised', overrelief='ridge')
        self.b_exportar.place(x=210, y=350)
 
    def formulario_evento(self):  
        self.l_evento = Label(janela, text='Evento*', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_evento.place(x=10, y=50)
        self.e_evento = Entry(janela , width =48, justify='left',relief='solid')
        self.e_evento.place(x=15, y=70)

        self.l_data = Label(janela, text='Data*', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_data.place(x=10, y=90)
        self.e_data = Entry(janela, width =40, justify='left',relief='solid')
        self.e_data.place(x=15, y=110)

        self.l_cid = Label(janela, text='Cidade*', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_cid.place(x=10, y=170)
        self.e_cid = Entry(janela, width =22,justify='left',relief='solid')
        self.e_cid.place(x=15, y=190)

        self.l_estado = Label(janela, text='Estado*', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_estado.place(x=158, y=170)
        self.e_estado = Entry(janela, width =5,justify='left',relief='solid')
        self.e_estado.place(x=168, y=190)

        self.l_local = Label(janela, text='Local*', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_local.place(x=10, y=130)
        self.e_local = Entry(janela, width =30,justify='left',relief='solid')
        self.e_local.place(x=15, y=150)

        self.l_espaco = Label(janela, text='Espaço*', anchor=NW, font=('Ivy 10 bold'),bg=c01,fg=c04, relief='flat')
        self.l_espaco.place(x=210, y=130)
        self.e_espaco = Entry(janela, width =14,justify='left',relief='solid')
        self.e_espaco.place(x=216, y=150)

        self.l_tipo = Label(janela, text='Tipo*', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_tipo.place(x=266, y=90)
        self.e_tipo = Entry(janela, width =5, justify='left',relief='solid')
        self.e_tipo.place(x=272, y=110)

        self.l_valor = Label(janela, text='Valor Ingresso*', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_valor.place(x=258, y=170)
        self.e_valor = Entry(janela, width =5, justify='left',relief='solid')
        self.e_valor.place(x=270, y=190)
            
        self.l_descricao = Label(janela, text='Descrição*', anchor=NW, font=('Ivy 10 bold'), bg=c01,fg=c04, relief='flat')
        self.l_descricao.place(x=10, y=250)
        self.e_descricao = Entry(janela, width =48, justify='left',relief='solid')
        self.e_descricao.place(x=15, y=270)

    def limpar_tela_evento(self):
        self.e_evento.delete(0, 'end')
        self.e_data.delete(0, 'end')
        self.e_cid.delete(0, 'end')
        self.e_estado.delete(0, 'end')
        self.e_local.delete(0, 'end')
        self.e_espaco.delete(0, 'end')
        self.e_tipo.delete(0, 'end')
        self.e_valor.delete(0, 'end')
        self.e_descricao.delete(0, 'end')
   
    def inserir_evento_tabela(self):
    ##### atualizar tabela #####
        evento = self.e_evento.get()
        data= self.e_data.get()
        cidade = self.e_cid.get()
        estado = self.e_estado.get()
        local = self.e_local.get()
        espaco = self.e_espaco.get()
        tipo = self.e_tipo.get()
        valor = self.e_valor.get()
        descricao = self.e_descricao.get()
        
        lista = [evento, data, cidade, estado, local, espaco, tipo, valor, descricao]

        if evento =='':
            messagebox.showerror('Erro', 'O nome não pode ser vario!')
        else:
            inserir_info(lista)    
            messagebox.showerror('Sucesso', "Os dados foram inseridos com sucesso!")

            self.e_evento.delete(0, 'end')
            self.e_data.delete(0, 'end')
            self.e_cid.delete(0, 'end')
            self.e_estado.delete(0, 'end')
            self.e_local.delete(0, 'end')
            self.e_espaco.delete(0, 'end')
            self.e_tipo.delete(0, 'end')
            self.e_valor.delete(0, 'end')
            self.e_descricao.delete(0, 'end')

                            
            #for widget in mostra_tabela_usuario().winfo_children():
                #widget.destroy()
            
            mostra_tabela_evento()

    def atualizar_tabela_evento(self):
        try:
            treev_dados = self.tree.focus()
            treev_dicionario = self.tree.item(treev_dados)
            tree_lista = treev_dicionario['values']

            valor_id = tree_lista[0]

            self.e_evento.delete(0, 'end')
            self.e_data.delete(0, 'end')
            self.e_cid.delete(0, 'end')
            self.e_estado.delete(0, 'end')
            self.e_local.delete(0, 'end')
            self.e_espaco.delete(0, 'end')
            self.e_tipo.delete(0, 'end')
            self.e_valor.delete(0, 'end')
            self.e_descricao.delete(0, 'end')
                
            self.e_evento.insert(0, tree_lista[1])
            self.e_data.insert(0, tree_lista[2])
            self.e_cid.insert(0, tree_lista[3])
            self.e_estado.insert(0, tree_lista[4])
            self.e_local.insert(0, tree_lista[5])
            self.e_espaco.insert(0, tree_lista[6])
            self.e_tipo.insert(0, tree_lista[7])
            self.e_valor.insert(0, tree_lista[8])
            self.e_descricao.insert(0, tree_lista[9])
            
            def update():    
                evento = self.e_evento.delete(0, 'end')
                data= self.e_data.delete(0, 'end')
                cidade = self.e_cid.delete(0, 'end')
                estado = self.e_estado.delete(0, 'end')
                local = self.e_local.delete(0, 'end')
                espaco = self.e_espaco.delete(0, 'end')
                tipo = self.e_tipo.delete(0, 'end')
                valor = self.e_valor.delete(0, 'end')
                descricao = self.e_descricao.delete(0, 'end')
                
                lista = [valor_id,evento, data, cidade, estado, local, espaco, tipo, valor, descricao]
                #or logradouro or num or bairro or cep or cidade or estado or idade or genero or telefone or cpf or email
                if evento  == '':
                    messagebox.showerror('Erro', 'Nenhum campo não pode ser vario!')

                #elif cpf == cpf:
                    #messagebox.showerror('Erro', 'CPF é unico por usuário!')

                else:
                    atualizar_info_evento(lista)
                    messagebox.showerror('Sucesso', "Os dados foram atualizados com sucesso!")

                    evento = self.e_evento.delete(0, 'end')
                    data= self.e_data.delete(0, 'end')
                    cidade = self.e_cid.delete(0, 'end')
                    estado = self.e_estado.delete(0, 'end')
                    local = self.e_local.delete(0, 'end')
                    espaco = self.e_espaco.delete(0, 'end')
                    tipo = self.e_tipo.delete(0, 'end')
                    valor = self.e_valor.delete(0, 'end')
                    descricao = self.e_descricao.delete(0, 'end')
                #for widget in mostra_tabela_usuario.winfo_children():
                    #widget.destroy()

                mostra_tabela_evento()
                    
        #### Botao para atualizar  ####
            
        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

    def deletar_tabela_evento(self):
        try:
            treev_dados = tree.focus()
            treev_dicionario = tree.item(treev_dados)
            tree_lista = treev_dicionario['values']

            valor_id = [tree_lista[0]]

            deletar_info_evento(valor_id)
            messagebox.showerror('Sucesso', "Os dados foram deletados da tabela com sucesso!")

            #for widget in mostra_tabela_usuario().winfo_children():
                #widget.destroy()
                
            mostra_tabela_evento()

        except IndexError:
            messagebox.showerror('Erro', 'Selecione um dos dados na tabela')

        mostra_tabela_evento()

def mostra_tabela_agenda():
    global tree
    ################ formatando tela a esquerda para apresentar a Tabela  ###############
    frame_direita= Frame(janela,bd=4, width=588, height=403, bg=c01, relief='flat') ### tela_apresenta
    frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW) ###frame.direita
    #********criando o visual da tabela a direita*******
    
        #Inserindo formulario de _evento
    cabecalho = ['ID','EVENTO','DATA','CIDADE','ESTADO','LOCAL','ESPAÇO','TIPO','VALOR INGRESSO','DESCRIÇÃO']
       
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=cabecalho, show="headings")

            #*********criando a barra de rolagem vertical*********
    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

            #*********criando a barra de rolagem horizontal*********
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

            #*********ativando a barra de rolagem*********
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

            #*********posicionando a barra de rolagem*********
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=3, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frame_direita.grid_rowconfigure(0,weight=12)

            #*****configurando as colunas da tabela
    hd=["nw","nw","nw","nw","nw","nw","nw","nw","nw","nw"]
    h=[20,150,150,100,100,100,100,100,100,100]
    n=0

    for coluna in cabecalho:
        tree.heading(coluna, text=coluna.title(),anchor=CENTER)
        tree.column(coluna,width=h[n],anchor=hd[n])
        n+=1

    lista = mostrar_info_evento()
    for item in lista:
        tree.insert('', 'end', values=item)
 


tela()