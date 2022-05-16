from string import hexdigits


print("Welcome to Rollercoaster Game")
height=int(input("What is your height in cm?"))

if height >= 120: # Jika tinggi badan lebih dari atau sama dengan 120
    print(f"Your height is {height} cm and you can ride the rollercoaster")

    # Kode dibawah ini adalah nested if, karena ada kondisi if didalam if
    age = int(input("What is your age? "))
    if (age >= 12 and age <=18 ) :
        print("Please pay 7$")
    elif age < 12 :
        print("Please pay 5$")
    else:
        print("Please pay 12$")
else:
    print(f"Your height is {height} cm, sorry you can't ride rollercoaster")
