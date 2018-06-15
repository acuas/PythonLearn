#This is a program that counts for a user
#The user enter the starting number, the ending number,
#and the amount by which to count.

start = int(input("Enter the starting number : "))
end = int(input("Enter the ending number : "))
amount = int(input("Enter the amount by which to count : "))


for i in range(start, end, amount):
    print(i, end=" ")
