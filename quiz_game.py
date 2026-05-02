print ("Welcome to my quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes" :
    quit()
else:    
    print("Okay! Let's play :)")

score = 0
    
answer = input ("What does CPU stand for? ")
if answer == "Central Processing Unit" : 
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Central Processing Unit.")
    

answer = input ("Name the capital city of Kenya? ")
if answer == "Nairobi" :
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Nairobi.")

print(f"You got {score} questions correct!")
print(f"You got {(score) / 2 * 100:.2f}% questions correct!")
