import tkinter as tk
from tkinter import ttk, messagebox
from packages.models.model_STOK import Loja, Produto
from packages.models.Mixins import SalvamentoMixin, CarregamentoMixin

class Login(SalvamentoMixin):
    def __init__(self, root, controller: 'Interface_Estoque'):
        self.root = root
        self.controller = controller
    
    def login(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill=tk.BOTH)

        tk.Label(self.frame, text="Olá, seja bem-vindo ao portal STOK. Primeiro, digite seu login:").grid(row=0, columnspan=2, pady=20)

        tk.Label(self.frame, text="Usuário:").grid(row=1, column=0)
        self.entry_usuario = tk.Entry(self.frame)
        self.entry_usuario.grid(row=1, column=1)

        tk.Label(self.frame, text="Senha:").grid(row=2, column=0)
        self.entry_senha = tk.Entry(self.frame, show="*")
        self.entry_senha.grid(row=2, column=1)

        tk.Button(self.frame, text="Entrar", command=self.verificar_login).grid(row=3, columnspan=2, pady=10)

    def verificar_login(self):
        usuario = self.entry_usuario.get()
        senha = self.entry_senha.get()

        if not usuario or not senha:
            messagebox.showerror("Aviso", "Você deve preencher todos os campos")
            return
        
        self.controller.login(usuario, senha)


class MenuPrincipal(CarregamentoMixin): 
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller

        self.frame_principal = tk.Frame(root)
        self.frame_principal.pack(fill=tk.BOTH, expand=True)

        self.construir_interface()

    def construir_interface(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()

        tk.Label(self.frame_principal, text="Menu Principal", font=("Arial", 16)).pack(pady=20)

        botoes = [
            ("Gerenciar Lojas", self.construir_interface_loja),
            ("Gerenciar Produtos", self.construir_interface_produto),
            ("Sair", self.sair_app) 
        ]

        for texto, comando in botoes:
            tk.Button(self.frame_principal, text=texto, command=comando, width=20).pack(pady=5)

    def construir_interface_loja(self):
        self.frame_loja = tk.Toplevel(self.root)
        self.frame_loja.title("Gerenciar Lojas")

        tk.Label(self.frame_loja, text="Nome").grid(row=1, column=0)
        self.entry_nome_loja = tk.Entry(self.frame_loja) 
        self.entry_nome_loja.grid(row=1, column=1)

        tk.Label(self.frame_loja, text="Endereço").grid(row=2, column=0)
        self.entry_endereco_loja = tk.Entry(self.frame_loja)
        self.entry_endereco_loja.grid(row=2, column=1)

        tk.Label(self.frame_loja, text="Email").grid(row=3, column=0)
        self.entry_email_loja = tk.Entry(self.frame_loja)
        self.entry_email_loja.grid(row=3, column=1)

        tk.Label(self.frame_loja, text="CNPJ").grid(row=4, column=0)
        self.entry_cnpj_loja = tk.Entry(self.frame_loja)
        self.entry_cnpj_loja.grid(row=4, column=1)

        tk.Label(self.frame_loja, text="Nicho").grid(row=5, column=0)
        self.entry_nicho_loja = tk.Entry(self.frame_loja)
        self.entry_nicho_loja.grid(row=5, column=1)

        tk.Button(self.frame_loja, text="Salvar", command=self.salvar_loja).grid(row=7, columnspan=2, pady=10)

        tk.Button(self.frame_loja, text="Dados salvos", command=self.carregar_loja_exibir).grid(row=8, columnspan=2, pady=10) # Renomeado para exibir os dados
        
        self.formatação_de_loja()

    def formatação_de_loja(self):
        self.tree_lojas = ttk.Treeview(self.frame_loja, columns=("Nome", "Endereço", "Email", "CNPJ", "Nicho"), show="headings")
        self.tree_lojas.heading("Nome", text="Nome")
        self.tree_lojas.heading("Endereço", text="Endereço")
        self.tree_lojas.heading("Email", text="Email")
        self.tree_lojas.heading("CNPJ", text="CNPJ")
        self.tree_lojas.heading("Nicho", text="Nicho")
        self.tree_lojas.grid(row=10, columnspan=2, pady=10)
        self.carregar_loja_exibir()

    def salvar_loja(self):
        nome = self.entry_nome_loja.get()
        endereco = self.entry_endereco_loja.get()
        email = self.entry_email_loja.get()
        cnpj = self.entry_cnpj_loja.get()
        nicho = self.entry_nicho_loja.get()

        if not all([nome, endereco, email, cnpj, nicho]):
            messagebox.showerror("Erro", "Todos os campos da loja devem ser preenchidos!")
            return

        loja_obj = Loja(self.entry_nome_loja, self.entry_endereco_loja, self.entry_email_loja, self.entry_cnpj_loja, self.entry_nicho_loja)
        
        dados_loja = loja_obj.formatacao_loja()
        
        lojas_existentes = self.controller.carregar_dados_lojas()
        lojas_existentes.append(dados_loja)

        if self.controller.salvar_dados_lojas(lojas_existentes):
            self.entry_nome_loja.delete(0, tk.END)
            self.entry_endereco_loja.delete(0, tk.END)
            self.entry_email_loja.delete(0, tk.END)
            self.entry_cnpj_loja.delete(0, tk.END)
            self.entry_nicho_loja.delete(0, tk.END)

    def carregar_loja_exibir(self):
        
        for item in self.tree_lojas.get_children():
            self.tree_lojas.delete(item)

        Dados_salvos_loja = self.controller.carregar_dados_lojas()
        if Dados_salvos_loja:
            for loja_data in Dados_salvos_loja:
                self.tree_lojas.insert("", tk.END, values=(
                    loja_data.get("Nome", ""),
                    loja_data.get("Endereço", ""),
                    loja_data.get("Email", ""),
                    loja_data.get("CNPJ", ""),
                    loja_data.get("Nicho", "")
                ))
        else:
            messagebox.showinfo("Informação", "Nenhuma loja encontrada.")


    def construir_interface_produto(self):
        self.frame_produto = tk.Toplevel(self.root)
        self.frame_produto.title("Gerenciar Produtos")

        tk.Label(self.frame_produto, text="Nome").grid(row=1, column=0)
        self.entry_nome_prod = tk.Entry(self.frame_produto)
        self.entry_nome_prod.grid(row=1, column=1)

        tk.Label(self.frame_produto, text="Tipo").grid(row=2, column=0)
        self.entry_tipo = tk.Entry(self.frame_produto)
        self.entry_tipo.grid(row=2, column=1)

        tk.Label(self.frame_produto, text="Marca").grid(row=3, column=0)
        self.entry_marca = tk.Entry(self.frame_produto)
        self.entry_marca.grid(row=3, column=1)

        tk.Label(self.frame_produto, text="Data de Fabricação").grid(row=4, column=0)
        self.entry_data = tk.Entry(self.frame_produto)
        self.entry_data.grid(row=4, column=1)

        tk.Label(self.frame_produto, text="Material").grid(row=5, column=0)
        self.entry_material = tk.Entry(self.frame_produto)
        self.entry_material.grid(row=5, column=1)

        tk.Label(self.frame_produto, text="Característica").grid(row=6, column=0)
        self.entry_caracteristica = tk.Entry(self.frame_produto)
        self.entry_caracteristica.grid(row=6, column=1)

        tk.Label(self.frame_produto, text="Quantidade").grid(row=7, column=0)
        self.entry_quantidade = tk.Entry(self.frame_produto)
        self.entry_quantidade.grid(row=7, column=1)

        tk.Button(self.frame_produto, text="Salvar", command=self.salvar_produto).grid(row=9, columnspan=2, pady=10)

        tk.Button(self.frame_produto, text="Dados salvos", command=self.carregar_produto_exibir).grid(row=10, columnspan=2, pady=10) # Corrigida a linha e o comando

        self.formatação_de_produto()

    def formatação_de_produto(self):
        self.tree_produtos = ttk.Treeview(self.frame_produto, columns=(
                "Nome do produto", "Tipo do Produto", "Marca do Produto", 
                "Data de Fabricação", "Material do produto", 
                "Característica do produto", "Quantidade do produto"
        ), show="headings")
        self.tree_produtos.heading("Nome do produto", text="Nome")
        self.tree_produtos.heading("Tipo do Produto", text="Tipo")
        self.tree_produtos.heading("Marca do Produto", text="Marca")
        self.tree_produtos.heading("Data de Fabricação", text="Data")
        self.tree_produtos.heading("Material do produto", text="Material")
        self.tree_produtos.heading("Característica do produto", text="Característica")
        self.tree_produtos.heading("Quantidade do produto", text="Quantidade")
        self.tree_produtos.grid(row=11, columnspan=2, pady=10)
        self.carregar_produto_exibir()

    def salvar_produto(self):
        nome = self.entry_nome_prod.get()
        tipo = self.entry_tipo.get()
        marca = self.entry_marca.get()
        data = self.entry_data.get()
        material = self.entry_material.get()
        caracteristica = self.entry_caracteristica.get()
        quantidade = self.entry_quantidade.get()

        if not all([nome, tipo, marca, data, material, caracteristica, quantidade]):
            messagebox.showerror("Erro", "Todos os campos do produto devem ser preenchidos!")
            return
        
        try:
            int(quantidade)
        except ValueError:
            messagebox.showerror("Erro", "A quantidade deve ser um número inteiro.")
            return

        produto_obj = Produto(self.entry_nome_prod, self.entry_tipo, self.entry_marca, 
                              self.entry_data, self.entry_material, 
                              self.entry_caracteristica, self.entry_quantidade)
        
        dados_produto = produto_obj.formatacao_produto()

        produtos_existentes = self.controller.carregar_dados_produtos()
        produtos_existentes.append(dados_produto)

        if self.controller.salvar_dados_produtos(produtos_existentes):
            self.entry_nome_prod.delete(0, tk.END)
            self.entry_tipo.delete(0, tk.END)
            self.entry_marca.delete(0, tk.END)
            self.entry_data.delete(0, tk.END)
            self.entry_material.delete(0, tk.END)
            self.entry_caracteristica.delete(0, tk.END)
            self.entry_quantidade.delete(0, tk.END)

    def carregar_produto_exibir(self):
        for item in self.formatação_de_produto.get_children():
            self.tree_produtos.delete(item)

        Dados_salvos_produto = self.controller.carregar_dados_produtos()
        if Dados_salvos_produto:
            for produto_data in Dados_salvos_produto:
                self.tree_produtos.insert("", tk.END, values=(
                    produto_data.get("Nome do produto", ""),
                    produto_data.get("Tipo do Produto", ""),
                    produto_data.get("Marca do Produto", ""),
                    produto_data.get("Data de Fabricação", ""),
                    produto_data.get("Material do produto", ""),
                    produto_data.get("Característica do produto", ""),
                    produto_data.get("Quantidade do produto", "")
                ))
        else:
            messagebox.showinfo("Informação", "Nenhum produto encontrado.")


    def sair_app(self):
        self.root.quit()