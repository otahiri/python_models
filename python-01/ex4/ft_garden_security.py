class Plant:
    def __init__(self, name: str, age: int, height: int):
        self.name = name
        print(f"Plant created: {self.name}")
        self.set_height(height)
        self.set_age(age)

    def set_age(self, age: int):
        if age > 0:
            self.__age = age

            print(f"Age updated: {self.__age} days [OK]")
        else:
            print(f"Invalid operation attempted: age {age}days [REJECTED]")
            print("Security: Negative age rejected")

    def get_age(self):
        return self.__age

    def set_height(self, height: int):
        if height > 0:
            self.__height = height
            print(f"Height updated: {self.__height}cm [OK]")
        else:
            print(f"\nInvalid operation attempted: height {height}cm \
[REJECTED]")
            print("Security: Negative height rejected\n")

    def get_height(self):
        return self.__height

    def get_info(self):
        print(f"Current plant: Rose ({self.get_height()}cm,\
 {self.get_age()} days)")


print("=== Garden Security System ===")
rose = Plant("Rose", 25, 30)
rose.set_height(-5)
rose.get_info()
