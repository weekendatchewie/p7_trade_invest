from bruteforce import brute_force


csv_file = open("./csv/action-test5.csv")


def run():
    print(brute_force(csv_file))


if __name__ == "__main__":
    run()
