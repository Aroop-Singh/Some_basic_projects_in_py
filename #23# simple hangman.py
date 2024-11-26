#23 simple hangman
import random

hangs = [
    # 1 wrong
    [
        "   ",
        "       ",
        "        ",
        "     _O_",
        "    __| ",
        "|  //[] "
    ],
    # 2 wrong
    [
        "   ",
        "       ",
        "        ",
        "      _O_",
        "|    __| ",
        "|   //[] "
    ],
    # 3 wrong
    [
        "   ",
        "       ",
        "        ",
        "|     _O_",
        "|    __| ",
        "|   //[] "
    ],
    # 4 wrong
    [
        "   ",
        "       ",
        "|        ",
        "|     _O_",
        "|    __| ",
        "|   //[] "
    ],
    # 5 wrong
    [
        "   ",
        "|      ",
        "|        ",
        "|     _O_",
        "|    __| ",
        "|   //[] "
    ],
    # 6 wrong
    [
        "______   ",
        "|       ",
        "|        ",
        "|     _O_",
        "|    __| ",
        "|   //[] "
    ],
    # 7 wrong
    [
        "______   ",
        "|    |   ",
        "|        ",
        "|     _O_",
        "|    __| ",
        "|   //[] "
    ],
    # 8 wrong
    [
        "______",
        "|    |",
        "|   _O_",
        "|    |",
        "|   //",
        "|   []"
    ],
    # 9 wrong
    [
        "______",
        "|    |",
        "|   _O_",
        "|    |",
        "|   //",
        "|   "
    ]
]

words= words = words = [
    "campfires", "discharge", "watchfire", "goldsmith", "overmatch", 
    "drumstick", "polymaths", "armchairs", "sculpting", "languides", 
    "blowziest", "earthling", "javelinos", "ploughers", "covariant", 
    "pictorial", "marvelous", "upgrowing", "ratifying", "importers"
]
word = random.choice(words)

# Frequency data for English letters
letter_frequencies = [
    ("E", 12.70), ("T", 9.06), ("A", 8.17), ("O", 7.51),
    ("I", 6.97), ("N", 6.75), ("S", 6.33), ("H", 6.09),
    ("R", 5.99), ("D", 4.25), ("L", 4.03), ("C", 2.78),
    ("U", 2.76), ("M", 2.41), ("W", 2.36), ("F", 2.23),
    ("G", 2.02), ("Y", 1.97), ("P", 1.93), ("B", 1.49),
    ("V", 0.98), ("K", 0.77), ("J", 0.15), ("X", 0.15),
    ("Q", 0.10), ("Z", 0.07)
]


loop = True
attempts = 9
guessed_letters = ["_"]*len(word)

while attempts > 0:
    print("\ncurrent : ", " ".join(guessed_letters))
    x= input("Enter your guessed letter(press * for hint): ").lower()
    if x in word:
        print("correcrt")
        for i in range(len(word)):
            if word[i] == x:
                guessed_letters[i] = x
    elif x == "*":
        # Print the table header
        print(f"\n{'Letter':<8}{'Frequency (%)':<15}{'Letter':<8}{'Frequency (%)':<15}")

        # Print the table in 4 columns
        for i in range(0, len(letter_frequencies), 2):
            letter1, freq1 = letter_frequencies[i]
            letter2, freq2 = letter_frequencies[i + 1]                                                                                  
            print(f"{letter1:<8}{freq1:<15}{letter2:<8}{freq2:<15}")
    else:
        print("##########incorrect##########" )
        attempts = attempts-1
        print(f"Remaining attempts: {attempts}")
        for hang in hangs[min(9 - attempts, len(hangs) - 1)]:
            print(hang)



    if "_" not in guessed_letters:
        print(f"\nCongratulations! You've guessed the word: {word}")
        break
    
    if attempts == 0:
        print(f"\nOut of attempts! The word was: {word}")

