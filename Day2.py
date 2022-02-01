Lottery  = "hello coders"

print("Choose correct character of the word '",Lottery,"' to win the lottery")
inputs = input("\n Word:- ").lower()

if inputs == "h" or inputs == "e" or inputs == "o" or inputs == "c" or inputs == "d":
    print("\n Congratulation You Win The Lottery")

else:
    print("\n Sorry You Didn't Win The Lottery")