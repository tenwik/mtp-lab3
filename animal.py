class Animal:
    """Базовый класс животного."""

    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        return "Животное издаёт звук"


class Dog(Animal):
    """Класс собаки, наследующий Animal."""

    def speak(self) -> str:
        return f"{self.name} говорит: Гав!"