from packages.models.model_STOK import Loja, Produto
from packages.models.Mixins import CarregamentoMixin, SalvamentoMixin, AlteracaoMixin
from packages.views.views_STOK import Login, MenuPrincipal
from tkinter import messagebox, ttk
import json

class Interface_Estoque(SalvamentoMixin):
    def __init__(self, root):
        self.root = root
        self.lojas = []  
        self.produtos = []

        self.root.after(100, self.login)
        self.view_login = Login(root, self)
        self.view_login.login()
        
    def login(self, usuario, senha):
        try:
                if usuario == "admin" and senha == "admin123":
                    for widget in self.root.winfo_children():
                        widget.destroy()
                        
                        self.view_menu = MenuPrincipal(self.root, self)
                        return True
                
                else:
                    messagebox.showerror("Erro", "Usuário ou senha inválidos!")
                    return False
        except Exception as e:
            messagebox.showerror("Erro", f"Falha no login: {str(e)}") 
            return False
        
    def salvar_cred(self, usuario, senha):
        dados = {"usuario":usuario, "senha":senha}
        try:
            with open("Dados_login.json", 'w') as file:
                json.dump(dados, file, indent=4)
            messagebox.showinfo("Sucesso", "Credenciais salvas com sucesso.")
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar credenciais: {str(e)}")

    def salvar_dados_lojas(self, dados_loja):
        return SalvamentoMixin.salvar("lojas.json", dados_loja)

    def carregar_dados_lojas(self):
        return CarregamentoMixin.carregar("lojas.json")

    def salvar_dados_produtos(self, dados_produto):
        return SalvamentoMixin.salvar("produtos.json", dados_produto)

    def carregar_dados_produtos(self):
        return CarregamentoMixin.carregar("produtos.json")

    def sair(self):
        if hasattr(self, 'view_menu') and self.view_menu:
            self.view_menu.quit()
        else:
            self.root.quit() 