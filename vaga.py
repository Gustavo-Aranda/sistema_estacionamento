class Vaga:
    def __init__(self, numero: int) -> None:
        self.numero = numero
        self.ocupada = False
        self.carro = None
    
    def estacionar(self, carro):
        if not self.ocupada:
            self.carro = carro
            self.ocupada = True
            print(f"Carro estacionado na vaga {self.numero}.")
        else:
            print("A vaga está ocupada.")
    
    def liberar(self):
        if self.ocupada:
            print(f"Vaga {self.numero} desocupada! Carro {self.carro.placa} saiu.")
            self.carro = None
            self.ocupada = False
        else:
            print("A vaga já está desocupada!")
    
    def __str__(self) -> str:
        return f'Vaga {self.numero} {"ocupada" if self.ocupada else "disponível"}'
    
