import sys, re

class ValidadorCPF:

    def __init__(self, CPF=None, multiplicador=None, listaCPF=None, calculo=None, indiceCPF=None):
        self.CPF: str = CPF
        self.multiplicador: int = 10
        self.listaCPF: list = listaCPF
        self.calculo: int = 0
        self.indiceCPF: int = 9
        if CPF is None: 
            self.solicitar_CPF()

    def solicitar_CPF(self):
        self.CPF: str = input('Digite o CPF aqui: ')
        self.CPF: str = re.sub(u'[-.]', '', self.CPF)
        self.listaCPF: list = list(self.CPF)
        self.manipulador()

    def manipulador(self):
        self.verificar_CPF()
        self.calcular_verificador()
        self.calcular_resto()
        self.validar_verificador()
        self.ajustar_valores()
        self.calcular_verificador()
        self.calcular_resto()
        self.validar_verificador()
        self.exibir_mensagem()

    def verificar_CPF(self):
        if self.CPF.isdecimal():
            if len(self.listaCPF) > 11 or len(self.listaCPF) < 11:
                print('CPF inválido.')
                sys.exit(0)
            else:
                pass
        else:
            self.CPF: str = re.sub('[0123456789]', '', self.CPF)
            print('Caracteres não compativeis: {}'.format(self.CPF))
            sys.exit(0)

    def calcular_verificador(self):
        for i in range(self.indiceCPF):
            self.calculo += self.multiplicador * int(self.listaCPF[i])
            self.multiplicador -= 1

    def calcular_resto(self):
        self.calculo %= 11
        if self.calculo == 0 or self.calculo == 1:
            self.calculo: int = 0
        else:
            self.calculo = 11 - self.calculo

    def validar_verificador(self):
        if self.calculo == int(self.listaCPF[self.indiceCPF]):
            pass
        else:
            print('CPF inválido.')
            sys.exit(0)

    def ajustar_valores(self):
        self.calculo: int = 0
        self.multiplicador: int = 11
        self.indiceCPF: int = 10

    def exibir_mensagem(self):
        print('CPF válido.')

validador = ValidadorCPF()