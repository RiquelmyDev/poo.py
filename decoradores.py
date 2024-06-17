'''decorador é um tipo de função que consegue modifcicar, 
ou estender outro tipo de função'''

from typing import Any


def meu_decorador(func):
  def wrapper():
    print("Antes da minha função ser chamada")
    func()
    print("Depois da minha função ser chamada")
  return wrapper  

@meu_decorador
def minha_funcao():
  print("Minha função foi chamada: ")

minha_funcao()

#Chamando decorador em classe

class MeuDecoradorDeClasse:
  def __init__(self, func) -> None:
    self.func = func

  def __call__(self) -> Any:
    print("Antes da minha função ser chamada decorador de classe")
    self.func()
    print("Depois da minha função ser chamada (decorador de classe)")

@MeuDecoradorDeClasse
def segunda_funcao():
  print("Segunda função foi chamada")

segunda_funcao()