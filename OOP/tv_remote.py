# Television program
import pickle


def open_file(file_name, mode):
    try:
        fin = open(file_name, mode)
        return fin
    except IOError:
        print("The file can't be opened!")
        exit(1)


class Tv(object):
    def __init__(self, channel=0, volume=25):
        self.__channel = channel
        self.__volume = volume

    @property
    def channel(self):
        return self.__channel

    @channel.setter
    def channel(self, value):
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.__channel = (value % 100)

    @property
    def volume(self):
        return self.__volume

    def raise_volume(self, value):
        if self.__volume + value <= 50:
            self.__volume += value
        else:
            self.__volume = 50

    def lower_volume(self, value):
        if self.volume - value >= 0:
            self.__volume -= value
        else:
            self.__volume = 0

    def __str__(self):
        tv_status = "Channel : " + str(self.__channel) + "\nVolume : " + str(self.__volume)
        return tv_status


class Drive(object):
    def __init__(self):
        fin = open_file("tv_date.dat", "rb")
        # Try to load file
        try:
            channel = pickle.load(fin)
            volume = pickle.load(fin)
            LG = Tv(channel, volume)
        except EOFError:
            LG = Tv()

        self.menu()
        while True:
            command = input("Enter a command : ")
            choice = 0
            no = 0
            if "+" in command:
                choice = 2
                for elem in command:
                    if elem != '+':
                        choice = 0
                        break
                if choice == 2:
                    no = len(command)
            elif "-" in command:
                choice = 3
                for elem in command:
                    if elem != '-':
                        choice = 0
                        break
                if choice == 3:
                    no = len(command)
            elif "q" in command:
                if len(command) == 1:
                    choice = 4
                else:
                    choice = 0
            else:
                choice = 1
                try:
                    no = int(command)
                except ValueError:
                    choice = 0

            if choice == 1:
                LG.channel = no
            elif choice == 2:
                LG.raise_volume(no)
            elif choice == 3:
                LG.lower_volume(no)
            elif choice == 4:
                break
            else:
                print("Invalid command!")

            print(LG)

    @staticmethod
    def menu():
        print(
        """
        1. To change the channel enter a number
        2. To raise volume of Tv enter '+' character 
        3. To decrease volume of Tv enter '-' character
        4. To shut down Tv enter 'q'
        """
        )


def main():
    D = Drive()


if __name__ == "__main__":
    main()
