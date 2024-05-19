"""POO, é um paradigma de progamação que se baseia
 na organização dos programas em torno de objetos. 
E basicamente objetos são instancias de classes"""

# Classe :
class Pessoa:
  def __init__(self, nome, idade) -> None:
    self.nome = nome
    self.idade = idade

  def saudacao(self):
    return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos" 

# Objetos
pessoa1 = Pessoa("Messi", 36)
mensagem = pessoa1.saudacao()

print (mensagem)

pessoa2 = Pessoa(nome="Ronaldo", idade=38)
mensagem = pessoa2.saudacao()
print (mensagem)
