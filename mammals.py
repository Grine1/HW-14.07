from animals import Animals

class Mammals(Animals):

  def __init__(self, animal: str, subtype: str):
    super().__init__(animal)
    self._subtype = subtype

  def __str__(self) -> str:
    return super().__str__() + f'\n  Subtype: {self._subtype}'