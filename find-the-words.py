#Use set to find the all different world

userInput = input()

#making it uppercase and removing white spaces
modifiedInput = userInput.upper().replace(" ", "")

wordFinder = set(modifiedInput)

print(wordFinder)