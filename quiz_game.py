print ("Welcome to my quiz game!")

playing = input("Do you want to play? ")

if playing.lower() != "yes" :
    quit()
else:    
    print("Okay! Let's play :)")
    
answer = input ("What does CPU stand for? ")
if answer == "Central Processing Unit" : 
    print("Correct!")
else:
    print("Incorrect! The correct answer is Central Processing Unit.")
    

answer = input ("Name the capital city of Kenya? ")
if answer == "Nairobi" :
    print("Correct!")
else:
    print("Incorrect! The correct answer is Nairobi.")