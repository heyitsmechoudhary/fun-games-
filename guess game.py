code_word = "nypd"
guess=""
guess_count = 0
guess_limit = 3
out_of_guess = False

while guess !=code_word and not  out_of_guess :
    if guess_count < guess_limit :
        guess=input("enter your guess : ") // enter INPUT
        guess_count += 1
    else :
        out_of_guess = True
if out_of_guess:
    print("out of guess YOU LOSE !") //output
else:
    print("Congorats YOU WIN !") //output
    
