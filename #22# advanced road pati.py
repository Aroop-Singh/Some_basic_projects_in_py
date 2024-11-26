#22 advanced road pati

import random

questions = [
    ["a. What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3, 1000, "Paris"],
    ["b. What color do you get when you mix red and white?", "Blue", "Purple", "Pink", "Green", 3, 2000, "Pink"],
    ["c. Which planet is known as the Red Planet?", "Earth", "Mars", "Venus", "Jupiter", 2, 5000, "Mars"],
    ["d. What is the largest mammal in the world?", "Elephant", "Blue Whale", "Giraffe", "Great White Shark", 2, 10000, "Blue Whale"],
    ["e. What is the freezing point of water?", "0 degrees Celsius", "32 degrees Celsius", "100 degrees Celsius", "-32 degrees Celsius", 1, 20000, "0 degrees Celsius"],
    ["f. Who wrote 'Romeo and Juliet'?", "Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen", 3, 40000, "William Shakespeare"],
    ["g. What is the main ingredient in guacamole?", "Tomato", "Avocado", "Lettuce", "Cucumber", 2, 80000, "Avocado"],
    ["h. How many continents are there?", "5", "6", "7", "8", 3, 160000, "7"],
    ["i. What is the capital of Japan?", "Beijing", "Seoul", "Tokyo", "Bangkok", 3, 320000, "Tokyo"],
    ["j. What gas do plants absorb from the atmosphere?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", 3, 640000, "Carbon Dioxide"],
    ["k. Who painted the Mona Lisa?", "Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Claude Monet", 3, 1250000, "Leonardo da Vinci"],
    ["l. What is the hardest natural substance on Earth?", "Gold", "Diamond", "Iron", "Quartz", 2, 2500000, "Diamond"],
    ["m. In which year did the Titanic sink?", "1912", "1905", "1920", "1898", 1, 5000000, "1912"],
    ["n. Which organ is responsible for pumping blood in the human body?", "Brain", "Liver", "Heart", "Lung", 3, 10000000, "Heart"],
    ["o. What is the capital of Australia?", "Sydney", "Melbourne", "Canberra", "Brisbane", 3, 70000000, "Canberra"]
]

lifelines = ["fifty-fifty","2 choice","expert"]
#print("\n#######################################################\nYou have 4 life lines: \nTRY AGAIN : you can try question again\n50-50 : 2 options will be eleminated\nDOUBLE CHOICE : you can choose 2 options\nEXPERT ADVICE : get right answer\n")
#print("REWARDS ARE:\n1,000\n2,000\n5,000\n10,000\n20,000\n40,000\n80,000\n1,60,000\n3,20,000\n6,50,000\n12,50,00\n25,00,000\n50,00,000\n1,00,00,000\n7,00,00,000\n")

i = 0            
loop = True
rand= (1,2,3,4)

def two_choice(): # chaaaat gpt
    print("Two choice lifeLine used!")
    first_choice = int(input("Enter your first answer: "))
    if first_choice == question[5]:
        print("Correct! Moving on...\n")
        a == question[5]  # Answer is correct
        return 1

    print("Incorrect! You have one more chance.")
    second_choice = int(input("Enter your second answer: "))
    if second_choice == question[5]:
        print("Correct! Moving on...\n")
        return 1  # Answer is correct

    print("Incorrect again. Game Over.")
    return 0

def fifty_fifty():
    print(f"\n{i+1}. Question for Rs. {question[6]} is:\n{question[0]}")
    print(f"option {question[5]} or option {random.choice(rand)}")

    second_choice = int(input("Enter your answer: "))
    if second_choice == question[5]:
        print("Correct! Moving on...\n")
        return 1  # Answer is correct
    else:
        print("Incorrect. Game Over.")
        return 0
    

def expert_advice():
    print(f"correct answer for question no.{i+1} is {question[5]}")

# main loop
while loop == True:
    question = questions[i]
    print(f"\n{i+1}. Question for Rs. {question[6]} is:\n{question[0]}")
    print(f"1. {question[1]}     2. {question[2]}")
    print(f"3. {question[3]}     4. {question[4]}"'\n')

# option input n check
    a = input("Enter option (press 5 for lifeline 6 to quit) : ")
    y = a.isdigit()
    while y == False:
        a = input("Enter option number : ")
        y = a.isdigit()
    a= int(a)

# answer check
    if a == question[5]:
        print(f"Correct answer you won {question[6]}\n ")
        i = i+1

# lifeline check
    elif a == 5:
        print(f"Avialable lifelines are- \n1.{lifelines[0]}\n2.{lifelines[1]}\n3.{lifelines[2]}")
        b = input("Enter your choice number : ")
        z = b.isdigit()
        while z == False:
            b = input("Enter option number : ")
            z = b.isdigit()
        b= int(b)
# fifty fifty loop
        if b == 1:
            print(f"You took {lifelines[0]}\n ")
            if fifty_fifty() == 1:
                print(f"Correct answer you won {question[6]}\n ")
                i = i+1
                
            else: 
                print("wrong answer\nGAME OVER\n")
                break

# 2 choice loop
        elif b == 2:
            print(f"You took {lifelines[1]}\n ")
            if two_choice() == 1:
                print(f"Correct answer you won {question[6]}\n ")
                i = i+1
                
            else: 
                print("wrong answer\nGAME OVER\n")
                break
# 3 expert advice loop
        elif b == 3:
            print(f"You took {lifelines[2]}\n ")
            expert_advice()

# quit check
    else:
        print("wrong answer\nGAME OVER\n")
        break

