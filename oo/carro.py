
"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade:
2) Método acelerar, que deverá incrementar a velocidade de uma unidade:
3) Método frear que deverá decrementar a velocidade em duas undiades:

A direção terá a responsabildade de controlar a direção. Ela oferece
os seguintes atributos:

1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste:
2) Método girar_a_direita
3) Método firar_a_esquerda

   N
O     L
   S

   Exemplo:
   >>> # Testando motor
   >>> motor = Motor()
   >>> motor.velocidade
   0
   >>> motor.acelerar()
   >>> motor.velocidade
   1
   >>> motor.acelerar()
   >>> motor.velocidade
   2
   >>> motor.acelerar()
   >>> motor.velocidade
   3
   >>> motor.frear()
   >>> motor.velocidade
   1
   >>> motor.frear()
   >>> motor.velocidade
   0
   >>> # Testando Direcao
   >>> direcao = Direcao()
   >>> direcao.valor
   'Norte'
   >>> direcao.girar_a_direta()
   >>> direcao.valor
   'Leste'
   >>> direcao.girar_a_direta()
   >>> direcao.valor
   'Sul'
   >>> direcao.girar_a_direta()
   >>> direcao.valor
   'Oeste'
   >>> direcao.girar_a_direta()
   >>> direcao.valor
   'Norte'
   >>> direcao.girar_a_esquerda()
   >>> direcao.valor
   'Oeste'
   >>> direcao.girar_a_esquerda()
   >>> direcao.valor
   'Sul'
   >>> direcao.girar_a_esquerda()
   >>> direcao.valor
   'Leste'
   >>> direcao.girar_a_esquerda()
   >>> direcao.valor
   'Norte'
   >>> carro = Carro(direcao, motor)
   >>> carro.calcular_velocidade()
   0
   >>> carro.calcular_acelear()
   >>> carro.calcular_velocidade()
   1
   >>> carro.calcular_acelear()
   >>> carro.calcular_velocidade()
   2
   >>> carro.calcular_frear()
   >>> carro.calcular_velocidade()
   0
   >>> carro.calcular_direcao()
   >>> 'Norte'
   >>> carro.girar_a_direita()
   >>> carro.calcular_direcao()
   >>> 'Leste'
   >>> carro.girar_a_esquerda()
   >>> carro.calcular_direcao()
   >>> 'Norte'
   >>> carro.girar_a_esquerda()
   >>> carro.calcular_direcao()
   >>> 'Oeste'

"""


class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'


class Direcao:

    rotacao_a_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }

    rotacao_a_esquerda_dct = {
        NORTE: OESTE, LESTE: NORTE, SUL: LESTE, OESTE: SUL
    }

    def __init__(self):
        self.valor = 'Norte'

    def girar_a_direta(self):
        self.valor = self.rotacao_a_direita_dct[self.valor]


if __name__ == '__main__':
    motor = Motor()
    print(motor.velocidade)

    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)

    direcao = Direcao()
    print(direcao.valor)
    direcao.girar_a_direta()
    print(direcao.valor)