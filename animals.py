class Animals(object):

  def __init__(self, animal: str):
    self._animal = animal

  def __str__(self) -> str:
    return f'\n> Animals: \n  animal: {self._animal}'
  