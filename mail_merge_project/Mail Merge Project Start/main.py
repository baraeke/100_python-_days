#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Open the starting letter template
with open('Input/Letters/starting_letter.txt', 'r') as starting_letter:
    letter_template = starting_letter.read() 

# Open the list of invited names
with open('Input/Names/invited_names.txt', 'r') as name_list:
    for name in name_list:
        name = name.strip()  # Remove any extra spaces or newline characters

        # Replace the placeholder with the actual name
        personalized_letter = letter_template.replace("[name]", name)

        # Write the personalized letter to a new file
        with open(f'Output/ReadyToSend/letter_for_{name}.txt', 'w') as letter:
            letter.write(personalized_letter)
