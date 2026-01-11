#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./Input/Letters/starting_letter.txt") as file:
    letters = file.read()

with open("./Input/Names/invited_names.txt") as file:
    names = file.readlines()
    for i, c in enumerate(names):
        names[i] = c.strip()

for person in names:
    data = "./Output/ReadyToSend/letter_for_" + person + ".txt"
    with open(data, mode='w') as file:
        temp = letters
        temp = temp.replace("[name]", person)
        file.write(temp)