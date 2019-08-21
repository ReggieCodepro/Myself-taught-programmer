#Challenge 1
Tv_list = ["The Walking Dead", "Entourge", "The Sopranos", "The Vampire Diaries"]
for Tv2 in Tv_list:
    print(Tv2)

#Challenge 2
for i in range(25, 51):
    print(i)
    
#Challenge 3
for item in Tv_list:
    print(Tv_list.index(item)+1,item)

#Challenge 4
num_list = [35, 32, 15, 1]


while True:
    ques = input("guess a number between 1 and 35. Press q to Quit: ")
    if ques == "q":
        print("You just quit game!")
        break
    try:
        ques = int(ques)
    except ValueError:
        print("Type a number or q to quit.")
    if ques in num_list:
        print("You got it right!")
    else:
        print("You guessed wrong, try again!")
              
#Challenge 5
list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
multiply = []
for i in list1:
    for j in list2:
        multiply.append(i * j)
print(multiply)
        

    
    
            
    

