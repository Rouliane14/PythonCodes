solution = "steal"
solution_letters = list(solution)
try_number = 1

while try_number<8:
    guess = input("Enter your 5-letter guess:")
    if len(guess)!=len(solution):
        guess = input("Seriously, 5-letter words only:")
    else:
        print("Checking your guess")

    guess_letters = list(guess)
    print(guess_letters)
    print(guess_letters[0])
    print(solution_letters[0])

    # first, check for blind luck
    if(guess==solution):
        print("🟩🟩🟩🟩🟩")
        print("Congratulations, you have solved Roulianedle in", try_number,"attempt(s)!")
        try_number=8

    else:
        # this should be the logic to check each letter of the guess word against the solution
        temp_solution_letters = solution_letters[:] 
        for i in range(4):
            hint = []
            if guess_letters[i] == solution_letters[i]:
                hint.append("🟩")
                temp_solution_letters.remove(guess_letters[i]) # remove one instance of the green letter from the pool to avoid a repeating letter in the guess turning to yellow
            elif guess_letters[i] in temp_solution_letters:
                k=solution_letters.index(guess_letters[i])
                if solution_letters[k]==guess_letters[k]:
                    hint.append("⬜️")
                else:
                    hint.append("🟨")
                    temp_solution_letters.remove(guess_letters[i]) # remove one instance of the yellow letter from the pool.
                # Shortcoming: this doesn't work when entering SPEED if solution is INTER.
                # First E of SPEED turns yellow, I need to check that when it finds guess(i) at position k in temp, that if guess(k) is not temp(k) then guess(i) is yellow, otherwise is blank.
            else:
                hint.append("⬜️")
            
        print(hint)
        try_number +=1
        if try_number<7:
            print("Starting Attempt number", try_number, "out of 7")
        else:
            print("Roulianedle has defeated you")
        


    

    


