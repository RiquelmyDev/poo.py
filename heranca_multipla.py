#herança simples
class Animal:
  def __init__(self, nome) -> None:
    self.nome = nome

  def emitir_som(self):
    pass

class Mamifero(Animal):
  def amamentar(self):
    return f"{self.nome} está amamentando"
  
class Ave(Animal):
  def voar(self):
    return f"{self.nome} está voando."

#herança multipla
class Morcego(Mamifero, Ave):
  def emitir_som(self):
    return "Morcegos emitem sons ultrassônicos"


morcego = Morcego(nome="Batman")
#Acessando os metodos da classe base ANIMAL

print("Nome do Morcego:", morcego.nome)
print ("Som do morcego: ", morcego.emitir_som())

# Assessando metodos da classe mamiferos e da classe Ave

print("Morcego amamentando: ", morcego.amamentar())
print("Morcego voando: ", morcego.voar())

