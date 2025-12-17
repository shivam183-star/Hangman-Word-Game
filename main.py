import random

words = ["apple", "banana", "orange", "grape", "peach", "mountain", "river", "cloud", "computer", 
         "python", "keyboard", "puzzle", "island", "universe", "galaxy", "jungle", "bottle", 
         "rocket", "window", "elephant""apple", "banana", "orange", "grape", "peach", "mountain", "river", "cloud", "computer",
"python", "keyboard", "puzzle", "island", "universe", "galaxy", "jungle", "bottle",
"rocket", "window", "elephant", "guitar", "ocean", "forest", "planet", "dream",
"castle", "dragon", "bridge", "camera", "shadow", "flower", "storm", "mirror",
"candle", "desert", "village", "garden", "snow", "school", "friend", "story",
"circle", "triangle", "square", "tiger", "lion", "zebra", "panda", "butterfly",
"rainbow", "sunshine", "moonlight", "star", "cloudy", "music", "violin", "drum",
"paint", "brush", "riverbank", "treasure", "pirate", "magic", "wizard", "giant",
"queen", "king", "prince", "princess", "fortune", "future", "history", "legend",
"temple", "monument", "island", "volcano", "earthquake", "tsunami", "festival",
"lantern", "balloon", "journey", "voyage", "explorer", "adventure", "compass",
"map", "mountain", "summit", "glacier", "valley", "canyon", "waterfall",
"diamond", "gold", "silver", "emerald", "sapphire", "crystal"]

word = random.choice(words)

n = len(word)
lives = n

print("Guess letters of the word")

result = [ '_' for i in range(0,n)]
for i in result:
    print(i, end=" ")

while '_' in result:
    print(f"\n{lives} lives left")
    if lives == 0:
        print("You failed ")
        print(f"Word was {word}")
        break
    
    w = input("Enter letter: ")

    if w in word:
        indexes = [i for i, val in enumerate(word) if val == w]
        for i in indexes:
            result[i] = w
    else:
        lives = lives-1

    for i in result:
        print(i, end=" ")
    
    if list(word) == result:
        print("\nYou found the word")


