# Lemonade Bar app


class Lemon(object):
    def __init__(self, number_lemon, sugar_cubes):
        self.__number_lemon = int(number_lemon)
        self.__sugar_cubes = int(sugar_cubes)
        self.__cash_amount = 0

    def drink_sweetened_lemonade(self):
        if self.__number_lemon > 0 and self.__sugar_cubes >= 2:
            self.__cash_amount += 2
            self.__sugar_cubes -= 2
            self.__number_lemon -= 1
        else:
            print("We are sorry, but we can't do a sweetened lemonade right now.")

    def drink_unsweetened_lemonade(self):
        if self.__number_lemon > 0:
            self.__number_lemon -= 1
            self.__cash_amount += 1
        else:
            print("We are sorry, but we can't do a unsweetened lemonade right now.")

    @property
    def cash_amount(self):
        return self.__cash_amount


class Drive(object):
    def __init__(self):
        nl = self.read_data("Enter the number of lemons : ")
        sc = self.read_data("Enter the number of sugar cubes : ")
        ob = Lemon(nl, sc)
        while True:
            self.menu()
            choice = 0
            try:
                choice = int(input("Choice : "))
            except ValueError:
                print("Could not convert data to int.")

            if choice == 1:
                ob.drink_sweetened_lemonade()
            elif choice == 2:
                ob.drink_unsweetened_lemonade()
            elif choice == 3:
                print(str(ob.cash_amount))
            elif choice == 4:
                break
            else:
                print("Invalid choice!")

    @staticmethod
    def read_data(prompt):
        nl = 0
        while True:
            try:
                nl = int(input(prompt))
                if nl >= 0:
                    break
                else:
                    raise ValueError("You can't have a negative number of lemons.")
            except ValueError as err:
                print(err.args)
        return nl

    @staticmethod
    def menu():
        print(
        """
        1. A sweetend lemonade
        2. A unsweetend lemonada
        3. Amount of cash
        4. Exit
        """
        )


def main():
    D = Drive()


if __name__ == '__main__':
    main()

