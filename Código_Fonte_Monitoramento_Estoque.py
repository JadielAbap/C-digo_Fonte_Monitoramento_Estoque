# Código_Fonte_Monitoramento_Estoque.py

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, nome, quantidade):
        if nome in self.produtos:
            self.produtos[nome] += quantidade
        else:
            self.produtos[nome] = quantidade

    def remover_produto(self, nome, quantidade):
        if nome in self.produtos:
            if self.produtos[nome] >= quantidade:
                self.produtos[nome] -= quantidade
            else:
                print(f"Quantidade insuficiente de {nome} no estoque.")
        else:
            print(f"{nome} não encontrado no estoque.")

    def consultar_estoque(self):
        for produto, quantidade in self.produtos.items():
            print(f"{produto}: {quantidade} unidades")

# Exemplo de uso
estoque_aquarela = Estoque()
estoque_aquarela.adicionar_produto("Pão", 100)
estoque_aquarela.adicionar_produto("Leite", 50)
estoque_aquarela.remover_produto("Pão", 20)
estoque_aquarela.consultar_estoque()
