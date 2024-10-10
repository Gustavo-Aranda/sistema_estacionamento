from datetime import datetime
from vaga import Vaga
from carro import Carro
class Estacionamento:
    def __init__(self, total_vagas: int):
        self.vagas = [Vaga(i+1) for i in range(total_vagas)]
    
    def estacionar_carro(self, carro: Carro):
        for vaga in self.vagas:
            if not vaga.ocupada:
                vaga.estacionar(carro)
                return
        print("Estacionamento cheio!")
        
    def liberar_vaga(self, placa: str, hora_saida: str):
        for vaga in self.vagas:
            if vaga.ocupada and (vaga.carro.placa == placa):
                tempo_permanencia = self.calcular_tempo(vaga.carro.hora_entrada, hora_saida)
                valor = self.calcular_valor(tempo_permanencia)
                vaga.liberar()
                print(f"Carro {placa} permaneceu {tempo_permanencia} minutos. Valor a pagar: R${valor:.2f}")
                return
        print("Carro não encontrado.")
        
    def calcular_tempo(self, hora_entrada: str, hora_saida: str) -> int:
        formato = "%H:%M"
        entrada = datetime.strptime(hora_entrada, formato)
        saida = datetime.strptime(hora_saida, formato)
        return (saida - entrada).seconds // 60

    def calcular_valor(self, tempo_permanencia: int) -> float:
        tarifa = 5.00 #Valor base tarifa
        horas = tempo_permanencia/60
        return max(tarifa, tarifa*horas)
    
    def status_vagas(self):
        for vaga in self.vagas:
            print(vaga)