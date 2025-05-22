import json
import os
from packages.models.Mixins import CarregamentoMixin, SalvamentoMixin, AlteracaoMixin

class Loja(CarregamentoMixin, SalvamentoMixin, AlteracaoMixin):
    def __init__(self, nome, endereco, email, cnpj, nicho):
        self._nome = nome
        self._endereco = endereco
        self._email = email
        self._cnpj = cnpj
        self._nicho = nicho

    def formatacao_loja(self):
        return {
            "Nome": self._nome.get(),
            "Endereço": self._endereco.get(),
            "Email": self._email.get(),
            "CNPJ": self._cnpj.get(),
            "Nicho": self._nicho.get()
        }
        
class Produto(CarregamentoMixin, SalvamentoMixin, AlteracaoMixin):
    def __init__(self, name, tipo, marca, data, material, caracteristica, quantidade):
        self._name = name
        self._tipo = tipo
        self._marca = marca
        self._data = data
        self._material = material
        self._caracteristica = caracteristica
        self._quantidade = quantidade

    def formatacao_produto(self):
        arquivo_produto = {
            "Nome do produto": self._name.get(),
            "Tipo do Produto": self._tipo.get(),
            "Marca do Produto": self._marca.get(),
            "Data de Fabricação": self._data.get(),
            "Material do produto": self._material.get(),
            "Característica do produto": self._caracteristica.get(),
            "Quantidade do produto": self._quantidade.get()
        }
        return arquivo_produto