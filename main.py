from algo_dynamic import algo_dynamic
from bruteforce import brute_force


def run():

    choices = {
        "1": algo_dynamic(),
        "2": brute_force(),
    }

    while True:
        print()
        print("Sélectionnez l'algorithme de votre choix :\n\n"
              "1 - Algorithme dynamique\n"
              "2 - Algorithme Force Brute\n"
              "Q - Quitter")
        asked = input(">>> ")
        print("\n")

        result = choices.get(asked)

        if asked == "q".lower():
            break

        elif asked not in choices:
            print("Sélectionnez une valeur correcte")

        else:
            print(result)


if __name__ == "__main__":
    run()
