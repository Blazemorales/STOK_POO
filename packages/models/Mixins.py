import json
import os 
from tkinter import messagebox

class SalvamentoMixin:
    def dict(self):
        return self.__dict__  
    @staticmethod 
    def salvar(arquivo, dados):
        try:
            with open(arquivo, 'w') as file:
                json.dump(dados, file, indent=4)
                messagebox.showinfo("Sucesso", "Seus dados foram salvos com sucesso")
            return True
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao salvar: {str(e)}")
            return False
        
class CarregamentoMixin:
    @staticmethod
    def carregar(arquivo):
        try:
            if not os.path.exists(arquivo):
                return []
            
            with open(arquivo, 'r') as f:
                dados = json.load(f)
                return dados
            
        except json.JSONDecodeError:
            messagebox.showerror("Erro", f"Falha ao carregar: Arquivo JSON inválido ou vazio: {arquivo}")
            return []
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao carregar: {str(e)}")
            return []
            
class AlteracaoMixin:
    def alterar(self, campo, novo_valor):
        if hasattr(self, campo):
            setattr(self, campo, novo_valor)
            return True
        return False