from typing import override


class RubberDuck:
    __color: str = "yellow"

    def __init__(self, volume=5) -> None:
        self.quack_volume: int = volume

    @staticmethod
    def squeak() -> None:
        print("duck is squeaking...")

    @classmethod
    def get_color(cls) -> str:
        return cls.__color

    @property
    def quack_volume(self) -> int:
        return self.__quack_volume

    @quack_volume.setter
    def quack_volume(self, value: int) -> None:
        self.__quack_volume = value

    def boost_volume(self) -> None:
        self.__quack_volume *= 2

    @override
    def __str__(self) -> str:
        return f"RubberDuck quack_volume={self.quack_volume} color={RubberDuck.__color}"

if __name__ == '__main__':

    duck = RubberDuck()
    print(duck)  #__str__

    RubberDuck.squeak()

    duck.quack_volume = 10
    print("🔊 New volume:", duck.quack_volume)

    duck.boost_volume()
    print("🚀 Boosted volume:", duck.quack_volume)

    print("🎨 Default color:", RubberDuck.get_color())