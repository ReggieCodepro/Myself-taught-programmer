#Challange 1
with open("did.txt", "r") as f:
    print(f.read())
    
#Challange 2
question = input("what is your favorite song?")
 
with open("fav_song.txt", "w") as f:
     f.write(question)

#Challange 3
import csv
List_one = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic", "The Revenant", "Inception"], ["Training Day", "Man on Fire", "Flight"]]
with open("List_one.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in List_one:
        spamwriter.writerow(List_one)
