solution = "seeds"
solution_letters = list(solution)
try_number = 1

while try_number<8:
    guess = input("Enter your 5-letter guess:")
    if len(guess)!=len(solution):
        guess = input("Seriously, 5-letter words only:")
    else:
        print("Checking your guess")

    guess_letters = list(guess)

    # first, check for blind luck
    if(guess==solution):
        print("🟩🟩🟩🟩🟩")
        print("Congratulations, you have solved Roulianedle in", try_number,"attempt(s)!")
        try_number=8

    else:
        # this should be the logic to check each letter of the guess word against the solution
        temp_solution_letters = solution_letters[:]
        hint = []
        for i in range(5):
            if guess_letters[i] == solution_letters[i]:
                hint.append("🟩")
                temp_solution_letters[i]="-"
                print(hint)
            else:
                hint.append("⬜️")  
                print(hint)
        print(temp_solution_letters)
        for i in range(5):
            if guess_letters[i] in temp_solution_letters and temp_solution_letters[i]!="-":
                hint[i]="🟨"
                temp_solution_letters[temp_solution_letters.index(guess_letters[i])]="^"
                print(hint)
                print(temp_solution_letters)
        
        
        print(hint[0],hint[1],hint[2],hint[3],hint[4])
        try_number +=1
        if try_number<7:
            print("Starting Attempt number", try_number, "out of 7")
        else:
            print("Roulianedle has defeated you")
        


    

    


