print("Welcome to the Mad Libs Generator!")
print("You will be asked for different words to create a funny story. Let's Go!\n")

while True:
    noun = input("Choose a noun: ")
    p_noun = input("Choose a plural noun: ")
    noun2 = input("Choose another noun: ")
    place = input("Choose a place: ")
    adjective = input("Choose an adjective(a describing word): ")
    noun3 = input("Choose another noun: ")

    print("\n---------------------------------")

    print(f"Be kind to your {noun} - footed {p_noun}. For a duck may be somebody's {noun2}. Be kind to your {p_noun} in {place}, where the weather is always {adjective}. You may think that this is the {noun3}. Well, it is!")

    play_again = input("Do you want to play again?(yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break