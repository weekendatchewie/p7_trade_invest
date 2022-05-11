from algo_dynamic import algo_dynamic
from bruteforce import brute_force

"""
Le même fichier est appelé deux fois dans deux variables différentes car sinon une erreur de type 
"IndexError: list index out of range" se déclenche
"""
csv_file1 = open("./csv/action-test5.csv")
csv_file2 = open("./csv/action-test5.csv")


def run():

    choices = {
        "1": algo_dynamic(csv_file1),
        "2": brute_force(csv_file1),
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
