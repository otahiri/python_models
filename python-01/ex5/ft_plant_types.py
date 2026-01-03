class Plant:
    """
    plant class that has 3 attributes
    name: the name of the plant
    age: the age of the plant
    height: the height of the plant
    """
    def __init__(self, name: str, age: int, height: int):
        """
        a constructor

        name: the name of the plant
        age: the age of the plant
        height: the height of the plant
        """
        self.name = name
        self.__age = 0
        self.__height = 0
        self.set_height(height)
        self.set_age(age)

    def set_age(self, age: int):
        """ set the age of the plant"""
        self.__age = age

    def get_age(self):
        """get the age of the plant"""
        return self.__age

    def set_height(self, height: int):
        """set the height of the plant"""
        self.__height = height

    def get_height(self):
        """get the height of the plant"""
        return self.__height


class Flower(Plant):
    """
    sub class of the super class Plant
    has the added attribute color of the flower
    """
    def __init__(self, name: str, color: str, age: int, height: int,
                 blooming: int):
        """
        a constructor

        name: the name of the plant
        color: the color of the plant
        age: the age of the plant
        height: the height of the plant
        """
        super().__init__(name, age, height)
        self.color = color
        self.blooming = blooming

    def get_info(self):
        """
        get the info of the plant such as age. color, name and height.
        """
        print(f"\n{self.name} ({__class__.__name__}): {self.get_height()}cm, \
{self.get_age()} days, {self.color} color")
        if self.blooming:
            print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """
    subclass of the super class Plant
    has the added of diameter of the tree
    """
    def __init__(self, name: str, diameter: int, age: int, height: int):
        """
        a constructor

        name: the name of the plant
        diameter: the diameter of the tree
        age: the age of the plant
        height: the height of the plant
        """
        super().__init__(name, age, height)
        self.diameter = diameter

    def get_info(self):
        """
        get the info of the plant such as the age, color name
        and how big the shade it provides
        """
        print(f"\n{self.name} ({__class__.__name__}): {self.get_height()}cm, \
{self.get_age()} days, {self.diameter}cm diameter")
        num = int(self.get_height()) // 100
        print(f"Oak provides {int(3.141592653589793 * (num**2))} square \
meters of shade")


class Vegetable(Plant):
    """
    subclass of the subclass plant
    has the added values
    vi: as in the vitamin the plant is rich int
    h_time: the harvest time
    """
    def __init__(self, name: str, h_time: str, nutrition: str, age: int,
                 height: int):
        """
        a constructor

        name: the name of the plant
        h_time: the harvest time of the plant
        vi: the vitamin the plant is rich in
        age: the age of the plant
        height: the height of the plant
        """
        super().__init__(name, age, height)
        self.harvest_time = h_time
        self.vitamin = nutrition

    def get_info(self):
        """
        get info about the plant such as name age height harvest time
        and the vitamin it is rich in
        """
        print(f"\n{self.name} ({__class__.__name__}): {self.get_height()}cm, \
{self.get_age()} days, {self.harvest_time} harvest")
        print(f"{self.name} is rich in vitamin {self.vitamin}")


print("=== Garden Plant Types ===")
rose = Flower("Rose", "red", 30, 25, 1)
rose.get_info()
oak = Tree("Oak", 50, 1825, 500)
oak.get_info()
tomato = Vegetable("Tomato", "summer", "C", 90, 80)
tomato.get_info()
