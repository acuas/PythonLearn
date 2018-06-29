class Complex(object):
    def __init__(self, re=0, im=0):
        try:
            re = float(re)
            re = float(re)
        except ValueError:
            print("Could not convert data to an float.")
            self.__re = float(0)
            self.__im = float(0)
        else:
            self.__re = re
            self.__im = im

    def __str__(self):
        string = str(self.__re)
        if self.__im == 0:
            return string
        else:
            return string + "+" + str(self.__im) + "*i"

    def __add__(self, other):
        return Complex(self.__re + other.__re, self.__im + other.__im)

    def __mul__(self, other):
        Re = self.__re * other.__re - self.__im * other.__im
        Im = self.__re * other.__im + self.__im * other.__re
        return Complex(Re, Im)


def main():
    z1 = Complex(6)
    z2 = Complex(2, 6)
    z3 = z1 * z2
    print(z3)


if __name__ == '__main__':
    main()
