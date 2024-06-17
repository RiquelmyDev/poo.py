# @classmethod
# @staticmethod

class MinhaClasse: # não consigo acessar a instancia direto da classe
  valor = 10 # Atributo de classe

  def __init__(self, nome) -> None: # isso aqui é uma instância
    self.nome = nome #Atributo da instância
  
  # requer uma instancia para ser chamado
  def metodo_instancia(self):
    return f"Método de instância chamado para {self.nome}"
  
  @classmethod # sempre que usar o decorador
  def metodo_classe(cls): #usar o ( CLS ), o CLS recebe a classe, ele pode alterar tudo. É como se fosse um adm, e o SELF o moderador
    return f"Método da classe chamado para valor={cls.valor}"

  @staticmethod
  def metodo_estatico(): # ele não recebe argumento, ele executa uma função especifica, não modifica nada
    return "Méttodo estático chamado"


obj = MinhaClasse(nome="(( exemplo)) ") # pra isso tenho que passar ela para um objeto, e ai sim acessar ela apartir do objeto

print(obj.metodo_instancia())
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

class Carro:
  def __init__(self, marca, modelo, ano) -> None:
    self.marca = marca
    self.modelo = modelo
    self.ano = ano

  @classmethod
  def criar_carro(cls, configuracao):
      marca, modelo, ano = configuracao.split(",")
      return cls(marca, modelo, int(ano)) # O retorno é uma instancia da classe carro


config1 = "Ferrari,f1,2023"
carro1 = Carro.criar_carro(config1)
print(f"Marca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")

config2 = "Porche,Panamera,2011"
carro2 = Carro.criar_carro(config2)
print(f"Marca: {carro2.marca}\nModelo: {carro2.modelo}\nAno: {carro2.ano}")


config3 = "Buggati,Veron,2020"
carro3 = Carro.criar_carro(config3)
print(f"Marca: {carro3.marca}\nModelo: {carro3.modelo}\nAno: {carro3.ano}")


class Matematica:

  @staticmethod
  def somar(a, b):
    return a + b

print(Matematica.somar(a=10, b=15))
