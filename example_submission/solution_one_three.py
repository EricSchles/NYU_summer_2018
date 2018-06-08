def prove(theorem):
    print("For the theorem")
    print(theorem)
    print("It is trival to show")
    print("And so the work is left as an exercise to the reader")

def get_theorem():
    print("Input a theorem to show")
    theorem = input()
    print()
    prove(theorem)

get_theorem()
