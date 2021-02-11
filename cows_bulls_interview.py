
import random
list1=[0,1,2,3,4,5,6,7,8,9]
i=0
list2=[]
list3=[]
list4=[]
while i < 5:
    random_number = random.choice(list1)
    if random_number not in list2:
        list2.append(random_number)
        i=i+1
print(list2,"ye secret list hain")
total_chances=10
count_of_chances=0
while count_of_chances<=total_chances:
    number=int(input("guess a number"))
    position=int(input("guess the position"))
    if (number in list2) and (list2.index(number) == position):
        list3.insert(position,number)
        print("guessed list",list3)
    elif (number in list2):
        if number not in list4:
            list4.append(number)
        print("These are correct numbers you can reuse it",list4)
    count_of_chances+=1 
    print("chances that you used",total_chances-count_of_chances)
    if list2==list3:
        print("you win the game")
        break
if list2==list3:
    print("you win the game")
else:
    print("you lose the game")