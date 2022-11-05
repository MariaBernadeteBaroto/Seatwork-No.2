#Seatwork-2

print('WELCOME')

name=input('Hi there, what is your name? ')

print('Okay', name,'Let us start!')


Array=[24, 88, 11, 3, 77, 11, 4, 24, 100, 4]

print(Array)


options=['Options:','1 - Add an element', '2 - Insert an element', '3 - Modify an element', '4 - Delete an element', 
           '5 - Arange the elements in Ascending order', '6 - Arrange the elements in Descending order', 
           '7 - Know the smallest number in the list', '8 - Know the largest number in the list', 
           '9 - Pop an element from the list', '10 - Get the sum of all the elements in the list']

for item in options:
    print(item)

while True:
    choice1 = input('select from the options:')
    if choice1.casefold()== '1':
        act1=int(input('Enter the number you want to add: '))
        Array.append(act1)
        print('This is your new Array:')
        print(Array)

    if choice1.casefold()=='2':
        act2=int(input('Enter the number you want to insert: '))
        act3=int(input('Enter the index you want it to insert: '))
        Array.insert(act3,act2)
        print('This is your new Array: ')
        print(Array)

    if choice1.casefold()=='3':
        act4=int(input('Enter the index of the element you want to Modify: '))
        act5=int(input('Enter the new number: '))
        Array[act4] = act5
        print('This is your new Array: ')
        print(Array)

    if choice1.casefold()=='4':
        act6=int(input('Enter the number you want to delete: '))
        Array.remove(act6)
        print('This is your new Array: ')
        print(Array)

    if choice1.casefold()=='5':
        Array.sort()
        print('This is your new Array: ')
        print(Array)

    if choice1.casefold()=='6':
        Array.sort(reverse=True)
        print('This is your new Array: ')
        print(Array)
    
    if choice1.casefold()=='7':
        smallest=min(Array)
        print('The smallest number in the list is: ', smallest)

    if choice1.casefold()=='8':
        largest=max(Array)
        print('The largest number in the list is: ', largest)

    if choice1.casefold()=='9':
        act7=int(input('Enter the index of the element you want to pop: '))
        num=Array.pop(act7)
        print(num)

    if choice1.casefold()=='10':
        total=sum(Array)
        print('The sum of all the elements in the list is ', total)

    choice2 = input('Do you want to select another option? (yes or no) : ')
    if choice2.casefold()=='no':
        print('Thank you!')
        break

