from animals import Animals

class Fish(Animals):

  def __init__(self, animal: str, name: str, group: str):
    super().__init__(animal)
    self._name = name
    self._group = group

  def __str__(self) -> str:
    return super().__str__() + f'\n  Name: {self._name} \n  Group: {self._group}'