#Importing random module in our code to generate random responses from computer"
import random

#Creating a Dictionary and assigning a emoji to the particular response to add more fun
dict={"r":"🪨", "p":"📃", "s":"✂️"}

#Created a List for error handling
list=("r","p","s")

while True:
        #Asking user to enter the choice and converting it in lower case to avoid case sensitivity
        User_choice=input("Enter your choice(r/p/s):").lower()

        #Genrating randome response from user
        Computer_Choice=random.choice(list)

        #Adding a loop to handle Invalid response unless we get a valid response from user
        while User_choice not in list:
                User_choice=input("Invalid output! Please enter your choice again (r/p/s):").lower()
        
        #Displaying user coice and computer choice
        print("Your choice:",dict[User_choice])
        print("Computer's choice:",dict[Computer_Choice])
        
        #Adding if else statement to dicide match result on the basis of user choice and computer choice
        if (User_choice=="r" and Computer_Choice=="s" or User_choice=="p"and Computer_Choice=="r" or User_choice=="s" and Computer_Choice=="p"):
                print("You won!😎")
        elif (User_choice=="r" and Computer_Choice=="r" or User_choice=="p"and Computer_Choice=="p" or User_choice=="s" and Computer_Choice=="s"):
                print("The match was draw!✌️")
        else:
                print("You Lost!🤭")

        #Asking user if he wishes to play again
        ask=input("Do you want to continue(y/n)?:")
        
        #Adding a loop to tackle Invalid response
        while ask not in ["y","n"]:
                ask=input("Invalid input! Do you want to continue(y/n)?:")

        if ask!="y":
                break

#Displaying greeting message when user tries to quit the game
print('Thank for playing 🙏')
     
    
 

              