#David
#assignment examples
#you can assignt values to variables by using an equals sign (right side goes into left side)
x=5

#when python read a variable ame, it replaces it with the variables stored value
y=x+5

# there are four different primitive datatypes

#integers: any whole number positive or negative
age = 15

#float: any number with a decimal, positive or negative
grade = 98.6

#string: human read-able characters
name = "David"

#numbers in a string are not numbers, they are letters
favoriteNumber = "69"

#boolean: true or false
#true is any value that ins not false or empty
isSmart= True

#you can output to the console by using 'print()'
print(age)
print(grade)
print(name)
print(favoriteNumber)
print(isSmart)

#you can have concatenate valuse together
print("My name " + name)
#you can use functions to convert datatypes
print("and my age is " + str(age))
#dont forget if you want to convert a value permanantly you must assign the converted value to a variable
age = str(age)
#you can convert back and forth with int(), str(), bool(), and float()
print(int(age))
print(float(age))
print(bool(age))
