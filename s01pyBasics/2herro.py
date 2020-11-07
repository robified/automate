# This program says herro and asks user for their name

print('Herro world!')

print('What is your name?') # ask for user's name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))

print('What is your age?') # ask for user's age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

len('Lobin') # 5
len('') # 0
len('Lobin') * 10 # 50

str(26) # '26'
int('123') # 123
float('3.14') # 3.14
float('1') # 1.0

int('26') + 1 # 27
str(27) + ' years old' # '27 years old'
