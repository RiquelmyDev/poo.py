import random

# Personagem: Classe mãe
# Heroi: controlado pelo usuario
# Inimigo: adversario do usuario

class Person:
  #atributos
  def __init__(self, name, life, level):
    self.__name = name
    self.__life = life
    self.__level = level

#metodos
  def get_name (self):
    return self.__name

  def get_life (self):
    return self.__life
  
  def get_level (self):
    return self.__level  

  def display_details(self):
    return f"Name: {self.get_name()}\nLife: {self.get_life()}\nLevel: {self.get_level()}"

  def receive_damage(self, damage):
    self.__life -= damage
    if self.__life < 0:
      self.__life = 0

  def attack(self, target):
    damage = random.randint(self.get_level() * 2, self.get_level() * 4) #baseado no nivel
    target.receive_damage(damage)
    print(f"{self.get_name()} atacou {target.get_name()} e causou {damage} de dano!")



# aqui usamos a herança e encapsulamento

class Hero(Person):
  def __init__(self, name, life, level, power):
    super().__init__(name, life, level)
    self.__power = power

  def get_power(self):
    return self.__power
  
  #polimorfismo
  def display_details(self):
    return f"{super().display_details()}\nPower: {self.get_power()}\n"
  
  def super_power(self, target):
    damage = random.randint(self.get_level() * 5, self.get_level() * 7)  #dano aumentado
    target.receive_damage(damage)
    print(f"{self.get_name()} usou a habilidade especial {self.get_power()} e causou {damage} de dano!")


class Enemy(Person):
  def __init__(self, name, life, level, type):
    super().__init__(name, life, level)
    self.__type = type

  def get_type(self):
    return self.__type
  
  def display_details(self):
    return f"{super().display_details()}\nType: {self.get_type()}"

class Game:
  """ Classe orquestradodora do jogo"""

  def __init__(self) -> None:
    self.hero = Hero(name="Batman", life=100, level=7, power="Super Strength")
    self.enemy = Enemy(name="Joker", life=100, level=13, type="danger")

  def ingnite_figth(self):
    """Fazer a gestão da batalha em turnos"""

    print("Start Figth!")
    while self.hero.get_life() > 0 and self.enemy.get_life() > 0:
      print("\n Person details:")
      print(self.hero.display_details())
      print(self.enemy.display_details())
      
      input("Press enter for attack...")
      escolha = input("Choise (1 - Normal Attack, 2 - Special Attack): ")

      if escolha == "1":
        self.hero.attack(self.enemy)

      elif escolha == "2":
        self.hero.super_power(self.enemy) 
      else:
        print("Invalid choise!")

      if self.enemy.get_life() > 0:
        #inimigo ataca o heroi
        self.enemy.attack(self.hero)  

    if self.hero.get_life() > 0:
      print("\n Congratulations, you win the figth!")
    else:
      print("\n i'am Sad, you defect the figth :/")  


""" Criar instância do jogo e iniciar baalha"""
game = Game()
game.ingnite_figth()


"""hero = Hero(name="Batman", life=100, level=7, power="Super Strength")
print(hero.display_details())

enemy = Enemy(name="Joker", life=50, level=15, type="danger")
print(enemy.display_details())"""