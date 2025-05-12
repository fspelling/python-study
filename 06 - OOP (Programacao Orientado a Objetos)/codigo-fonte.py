# Criando a primeira classe
class Funcionario:
    nome: str
    sobrenome: str

func1 = Funcionario()
func1.nome = 'Fernando'
func1.sobrenome = 'Spelling'

print(func1.nome)

# Classe com contrutores
class Funcionario:
    def __init__(self, nome: str, sobrenome: str):
        self.nome = nome
        self.sobrenome = sobrenome

    def to_string(self) -> str:
        return f'{self.nome} {self.sobrenome}'

func = Funcionario('Fernando', 'Spelling')

print(func.to_string())
print(Funcionario.to_string(func))
