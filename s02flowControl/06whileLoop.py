# while loop example 1
spam = 0
while spam < 5:
    print('Herro world!')
    spam = spam + 1


# while loop example 2
name = ''
while name != 'your name':
    print('Please type your name')
    name = input()
print('Thank you!')


# infinite loop
while True:
    print('LULZ!')


# break statement
while True:
    print('Please type your name')
    name = input()
    if name == 'your name':
        break
print('Thank you!')


# continue statement
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))