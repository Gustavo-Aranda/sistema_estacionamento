class Carro:
    def __init__(self, placa:str, modelo:str, hora_entrada:str) -> None:
        self.placa = placa
        self.modelo = modelo
        self.hora_entrada = hora_entrada
    
    def __str__(self) -> str:
        return f"Carro: {self.modelo} - Placa: {self.placa}"
