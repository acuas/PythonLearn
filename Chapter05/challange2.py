# Character Creator program

print("What is the name of your character?")
name = input("The name of my character is : ")

print("Ok", name + ",", "now it's time to choose what attributes to increase.")
attributes = {"Strength": 1,
              "Health": 1,
              "Wisdom": 1,
              "Dexterity": 1}

points = 30
choice = None
while choice != "0":
    print("You have", points, "points to spend on attributes.")
    print(attributes)
    print(
    """
    0. Continue
    1. Strength
    2. Health
    3. Wisdom
    4. Dexterity
    """
    )

    choice = input("Choice: ")
    choice2 = None
    if choice == "0":
        break
    elif choice == "1":
        while choice2 != "0":
            print(
            """
            0. Go back
            1. Increase strength
            2. Decrease strength
            """
            )
            choice2 = input("Choice: ")
            if choice2 == "0":
                break
            elif choice2 == "1" and points > 0:
                ok = "0"
                while ok == "0":
                    no = int(input("Enter the number of points you want to add :"))
                    if 0 < no <= points:
                        attributes["Strength"] += no
                        points -= no
                        ok = "1"
                    else:
                        print("The number of points that you want to add is invalid!")
                        print("You need to choose a number between 1 and", points)
            elif choice2 == "2" and attributes["Strength"] > 1:
                ok = "0"
                while ok == "0":
                    no = int(input("Enter the number of points you want to substract :"))
                    if attributes["Strength"] - no >= 1:
                        attributes["Strength"] -= no
                        points += no
                        ok = "1"
                    else:
                        print("The number fo points that you want to substract is invalid!")
                        print("You need to choose a number between 1 and", attributes["Strength"] - 1)
            else:
                print("Invalid choice\n")
    elif choice == "2":
        while choice2 != "0":
            print(
            """
            0. Go back
            1. Increase health
            2. Decrease health
            """
            )
            choice2 = input("Choice: ")
            if choice2 == "0":
                break
            elif choice2 == "1" and points > 0:
                ok = "0"
                while ok == "0":
                    no = int(input("Enter the number of points you want to add :"))
                    if 0 < no <= points:
                        attributes["Health"] += no
                        points -= no
                        ok = "1"
                    else:
                        print("The number of points that you want to add is invalid!")
                        print("You need to choose a number between 1 and", points)
            elif choice2 == "2" and attributes["Health"] > 1:
                ok = "0"
                while ok == "0":
                    no = int(input("Enter the number of points you want to substract :"))
                    if attributes["Health"] - no >= 1:
                        attributes["Health"] -= no
                        points += no
                        ok = "1"
                    else:
                        print("The number fo points that you want to substract is invalid!")
                        print("You need to choose a number between 1 and", attributes["Health"] - 1)
            else:
                print("Invalid choice\n")
    elif choice == "3":
        while choice2 != "0":
            print(
            """
            0. Go back
            1. Increase Wisdom
            2. Decrease Wisdom
            """
            )
            choice2 = input("Choice: ")
            if choice2 == "0":
                break
            elif choice2 == "1" and points > 0:
                ok = "0"
                while ok == "0":
                    no = int(input("Enter the number of points you want to add :"))
                    if 0 < no <= points:
                        attributes["Wisdom"] += no
                        points -= no
                        ok = "1"
                    else:
                        print("The number of points that you want to add is invalid!")
                        print("You need to choose a number between 1 and", points)
            elif choice2 == "2" and attributes["Wisdom"] > 1:
                ok = "0"
                while ok == "0":
                    no = int(input("Enter the number of points you want to substract :"))
                    if attributes["Wisdom"] - no >= 1:
                        attributes["Wisdom"] -= no
                        points += no
                        ok = "1"
                    else:
                        print("The number fo points that you want to substract is invalid!")
                        print("You need to choose a number between 1 and", attributes["Wisdom"] - 1)
            else:
                print("Invalid choice\n")
    elif choice == "4":
        while choice2 != "0":
            print(
            """
            0. Go back
            1. Increase Dexterity
            2. Decrease Dexterity
            """
            )
            choice2 = input("Choice: ")
            if choice2 == "0":
                break
            elif choice2 == "1" and points > 0:
                ok = "0"
                while ok == "0":
                    no = int(input("Enter the number of points you want to add :"))
                    if 0 < no <= points:
                        attributes["Dexterity"] += no
                        points -= no
                        ok = "1"
                    else:
                        print("The number of points that you want to add is invalid!")
                        print("You need to choose a number between 1 and", points)
            elif choice2 == "2" and attributes["Dexterity"] > 1:
                ok = "0"
                while ok == "0":
                    no = int(input("Enter the number of points you want to substract :"))
                    if attributes["Dexterity"] - no >= 1:
                        attributes["Dexterity"] -= no
                        points += no
                        ok = "1"
                    else:
                        print("The number fo points that you want to substract is invalid!")
                        print("You need to choose a number between 1 and", attributes["Dexterity"] - 1)
            else:
                print("Invalid choice\n")
    else:
        print("Invalid choice!\n")
