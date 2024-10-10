from estacionamento import Estacionamento
from carro import Carro

estacionamento = Estacionamento(4)

carro1 = Carro("ABC-1234", "Honda Civic", "12:00")
carro2 = Carro("DEF-5678", "Fuscao Preto", "09:00")
carro3 = Carro("GHI-9012", "BYD blablabla", "15:00")

estacionamento.estacionar_carro(carro1)
estacionamento.estacionar_carro(carro2)
estacionamento.estacionar_carro(carro3)

estacionamento.status_vagas()

estacionamento.liberar_vaga("DEF-5678", "12:31")

carro4 = Carro("JKL-3456", "Lamborghini", "12:32")
estacionamento.estacionar_carro(carro4)
