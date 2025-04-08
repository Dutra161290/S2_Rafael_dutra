class LojaAlimentos:
    def __init__(self):
        self.produtos = {
            "Arroz": 5.00,
            "Feijão": 4.50,
            "cavalo": 3.00,
            "ninja roberto": 6.20
        }

    def mostrar_produtos(self):
        print("cavalos disponíveis na loja:")
        for produto, preco in self.produtos:
            print(f"{produto}: R${preco}")

    def calcular_total(self, items):
        total = 0
        for item in items:
            total += self.produtos[item]
        return total

loja = LojaAlimentos()

loja.mostrar_produtos()

itens_comprados = ["Arroz", "Feijão", "Óleo"]
total = loja.calcular_total(itens_comprados)
print(f"Total do roberto seu nome : R${total}")
