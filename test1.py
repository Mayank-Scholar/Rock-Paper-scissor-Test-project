import random
dict={"r":"🪨", "p":"📃", "s":"✂️"}
list=("r","p","s")

while True:
        User_choice=input("Enter your choice(r/p/s):").lower()
        Computer_Choice=random.choice(list)
        
        while User_choice not in list:
                User_choice=input("Invalid output! Please enter your choice again (r/p/s):").lower()

        print("Your choice:",dict[User_choice])
        print("Computer's choice:",dict[Computer_Choice])

        if (User_choice=="r" and Computer_Choice=="s" or User_choice=="p"and Computer_Choice=="r" or User_choice=="s" and Computer_Choice=="p"):
                print("You won!😎")
        elif (User_choice=="r" and Computer_Choice=="r" or User_choice=="p"and Computer_Choice=="p" or User_choice=="s" and Computer_Choice=="s"):
                print("The match was draw!✌️")
        else:
                print("You Lost!🤭")

        ask=input("Do you want to continue(y/n)?:")

        while ask not in ["y","n"]:
                ask=input("Invalid input! Do you want to continue(y/n)?:")

        if ask!="y":
                break

print('Thank for playing 🙏')
     
    
 

              