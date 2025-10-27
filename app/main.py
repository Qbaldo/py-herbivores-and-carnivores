class Animal:
    alive = []

    def __init__(self,
                 name: str,
                 health: int = 100,
                 hidden: bool = False,
                 ) -> None:

        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive = True
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (f"{{Name: {self.name}, Health: "
                f"{self.health}, Hidden: {self.hidden}}}")


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if (target.alive and isinstance(target, Herbivore)
                and not target.hidden):
            target.health -= 50
            if target.health <= 0:
                if target in Animal.alive:
                    target.alive = False
                    Animal.alive.remove(target)
