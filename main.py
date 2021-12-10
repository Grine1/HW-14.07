from birds import Birds
from fish import Fish
from legs import Legs


if __name__ == '__main__':

  dog = Legs('Тварина', 'Чотирьох лапі', 'Собака')
  cat = Legs('Тварина', 'Чотирьох лапі', 'Кіт')
  bird = Birds('Тварина', 'Ястріб', 'Птахи', 'Ястребообразні')
  fish = Fish('Тварина', 'Окунь', 'Риба')

  print(dog)
  print(cat)
  print(bird)
  print(fish)