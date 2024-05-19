# Exemplo herança

print("\n Exemplo de herança:")
class Animal:
  def __init__(self, nome) -> None:
    self.nome = nome
  
  def andar(self):
    print(f"O animal {self.nome} andou")
    return
  
  def emitir_som(self):
    pass

class Cachorro(Animal):
  def emitir_som(self):
    return "Au, au"
  
class Gato(Animal):
  def emitir_som(self):
    return "Miau" 
  

dog = Cachorro(nome="Rex")
cat = Gato(nome="Juquinha")

print("\nExemplo de polimorfirsmo")
animais = [dog, cat]

for animal in animais:
  print(f"{animal.nome} faz: {animal.emitir_som()}")

#Exemplo de encapsulamento

print("\n Exemplo de encapsulamento:")
class ContaBancaria:
  def __init__(self, saldo) -> None:
    self.__saldo = saldo #Atributo privado

  def depositar(self, valor):
    if valor > 0:
      self.__saldo += valor

  def sacar(self, valor):
    if valor > 0 and valor <= self.__saldo:
      self.__saldo -= valor

  def consultar_saldo(self):
    return self.__saldo
  
conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.depositar(valor=500)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor=1000)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")
conta.sacar(valor=200)
print(f"Saldo da conta bancária: {conta.consultar_saldo()}")

conta_Kaio = ContaBancaria(saldo=100)

#abstração

print("\n Exemplo de Abstração:")
from abc import ABC, abstractmethod

class Veiculo(ABC):
  
  @abstractmethod
  def ligar(self):
    pass

  @abstractmethod
  def desligar(self):
    pass

class Carro(Veiculo):
  def __init__(self) -> None:
    pass

  def ligar(self):
    # Ligação do carro
    return "Carro ligado usando a chave!"

  def desligar(self):
    return "carro desligado usando a chave!"
  
porche_panamera = Carro()
print (porche_panamera.ligar())
print (porche_panamera.desligar())


