from mammals import Mammals

class Legs(Mammals):

  def __init__(self, animal: str, subtype: str, name: str):
    super().__init__(animal, subtype)
    self._name = name

  def __str__(self) -> str:
    return super().__str__() + f'\n  Name: {self._name}'