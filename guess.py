while True:

    guess = input("Guess a number (Input q to quit): ")



    try:

        if (guess == "q" or guess == "Q"):

            print("Goodbye!")

            print("")

            break;

        else:

            int(guess)

            if int(guess) == 18:

                print("You got it!")

                print("")

                break;

            else:

                print("Try again!")

                print("")

    except:

        print("Please input a number!")
        print("")
