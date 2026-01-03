class Plant:
    """
    plant class
    attributes:
    name: the name of the plant
    age: the age of the plant in days
    height: the height of the plant in cm
    """
    def __init__(self, name: str, age: int, height: int) -> None:
        """
        a constructor
        name: the name of the plant
        age: the age of the plant
        height: the height of the plant
        """
        self.name = name
        print(f"Plant created: {self.name}")
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def set_age(self, age: int):
        """
        set the age of the plant
        rejects all invalid ages
        age: the age of the plant
        """
        if age > 0:
            self.__age = age
            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age}days [REJECTED]")
            print("Security: Negative age rejected")

    def get_age(self):
        """
        return the age of the plant
        """
        return self.__age

    def set_height(self, height: int):
        """
        set the height of the plant
        rejects all invalid height
        height: the height of the plant
        """
        if height > 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"\nInvalid operation attempted: height {height}cm \
[REJECTED]")
            print("Security: Negative height rejected\n")

    def get_height(self):
        """
        return the height of the plant
        """
        return self.__height

    def get_info(self):
        """
        print info about the plant
        """
        print(f"Current plant: Rose ({self.get_height()}cm,\
 {self.get_age()} days)")


print("=== Garden Security System ===")
rose = Plant("Rose", 30, 25)
rose.set_height(-5)
rose.get_info()
