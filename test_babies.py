import csv

# TODO: Parse CSV in compliance with chosen polaroid distribution method.


def test_babies():
    filename = "babies.csv"

    with open(filename, 'r') as data:
        for line in csv.DictReader(data):
            print(line)


if __name__ == "__main__":
    test_babies()
