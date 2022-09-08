print("Welcome to Rollercoaster Game")
height=int(input("What is your height in cm?"))
bill=0

if height >= 120: # Jika tinggi badan lebih dari atau sama dengan 120
    print(f"Your height is {height} cm and you can ride the rollercoaster")

    # Kode dibawah ini adalah nested if, karena ada kondisi if didalam if
    age = int(input("What is your age? "))
    if (age >= 12 and age <=18 ) :
        bill=7
        print("Please pay 7$")
    elif age < 12 :
        bill=5
        print("Please pay 5$")
    else:
        bill=12
        print("Please pay 12$")
    
    wants_photo=input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y" :
        #Add 3$ bill
        bill+=3
    
    print(f"Your bill is {bill}")

else:
    print(f"Your height is {height} cm, sorry you can't ride rollercoaster")
