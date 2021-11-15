#David
#practice using expression and conditional statements

#An expression is a problem that must be solved
# 5+5 is an "arithmetic" expression
x = 5 + 5

#functions/mmethods must be resolved as expressions as well
answer = input("what is your name?")

#Comparison expressions resolve as true/false
print( 7 > 7 )
print( 7 >=  7)
print( x == 10 )
print( x > 10 or x <10 )

#A conditional statement runs if its condition is true / not false
if answer == "Bob":
    print("Hello, Bob! welcome back!")
    print("this line also prints if your name is Bob")
elif answer == "vadim":
    print("hey! you still owe me money!")
    
else:
    print("Sorry, I only talk to Bobs")
#print("this line isnt inside of the if statement, and prints regardless")

# ^ if checks a condition
# ^ Elif checks a condition if the previous conditions were not true
# ^ you can have as many elifs as you want
# ^ else runs if no prior condition were true

age = input("What is your age")
age = int(age)
if age == x >= 10:
    print("You can get your pokemon license")
elif age == 9:
    print("You have one more year to get your license")
else:
    print("sorry you are too young to get your license")

