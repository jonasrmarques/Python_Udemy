class Funcionario:
    def __init__(self, nome="indigente", salario_base=1000.20):
        self.nome = nome
        self.salario = salario_base
    
    def calcular_salario(self):
        return self.salario


class FuncionarioComum(Funcionario):

    def __init__(self, nome, salario_base):
        super().__init__(nome, salario_base)
    
    
class Gerente(Funcionario):
    def __init__(self, nome, salario_base, bonificacao):
        super().__init__(nome, salario_base)
        self.bonificacao = bonificacao
        
    def calcular_salario(self):
        return self.salario + self.bonificacao
    

class Desenvolvedor(Funcionario):
    def __init__(self,nome, salario_base, bonus):
        super().__init__(nome, salario_base)
        self.bonus = bonus
    
    def calcular_salario(self):
        return self.salario + self.bonus




lista_de_funcionarios = [Gerente("Fabio", 1500, 200), Desenvolvedor("Jonas", 1000, 100), FuncionarioComum("Alberto", 1200)]

for funcionario in lista_de_funcionarios:
    print(funcionario.calcular_salario())