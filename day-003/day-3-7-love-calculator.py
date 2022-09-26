# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
new_name1 = name1.lower()
new_name2 = name2.lower()
merge_name = new_name1 + new_name2

T = merge_name.count('t')
R = merge_name.count('r')
U = merge_name.count('u')
E = merge_name.count('e')
L = merge_name.count('l')
O = merge_name.count('o')
V = merge_name.count('v')
first_digit = int(T+R+U+E)
second_digit = int(L+O+V+E)
love_score = str(first_digit) + str(second_digit)
#print (f"Love score {love_score}")
int_love_score = int(love_score)
if int_love_score < 10 or int_love_score > 90:
  print (f"Your score is {int_love_score}, you go together like coke and mentos")
elif int_love_score > 40 and int_love_score <50:
  print (f"Your score is {int_love_score}, you are alright together")
else:
  print (f"Your score is {int_love_score}")