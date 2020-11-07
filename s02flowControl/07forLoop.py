# for loop example 1
print('My name is')
for i in range(5):
    print('Lobin Five Time ' + str(i))


# for loop example 2
total = 0
for num in range(101):
    total = total + num
print(total) # 5050


# can use a while loop to do the same thing as a for loop
print('My name is')
i = 0
while i < 5:
    print('Lobin Five Time ' + str(i))


# for loop with range example 
range(10) # range(0, 10)
print('My name is')
for i in range(12, 16):
    print('Lobin Five Time ' + str(i))


# for loop with step argument
# stepping up
print('My name is')
for i in range(0, 11, 2):
    print('Lobin Five Time ' + str(i))

# stepping down
print('My name is')
for i in range(5, -1, -1):
    print('Lobin Five Time ' + str(i))