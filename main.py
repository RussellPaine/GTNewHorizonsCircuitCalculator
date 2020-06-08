"""Simple program to figure out the
    best and easiest circuit to make
"""
import csv

class items():
    circuits = {}
    items = {}

class craft():
    def __init__(self, _n, _i1, _i2, _i3, _i4, _i5, _i6, _i7, _i8, _i9, _n1, _n2, _n3, _n4, _n5, _n6, _n7, _n8, _n9, _machine, _y):
        name = n
        i1 = _i1
        i2 = _i2
        i3 = _i3
        i4 = _i4
        i5 = _i5
        i6 = _i6
        i7 = _i7
        i8 = _i8
        i9 = _i9
        n1 = _n1
        n2 = _n2
        n3 = _n3
        n4 = _n4
        n5 = _n5
        n6 = _n6
        n7 = _n7
        n8 = _n8
        n9 = _n9
        machine = _machine
        y = _y

def read_in_values():
    """Reads in items from CSV
    """

    structure = 

    csv_reader = 0
    with open('items.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            else:
                print(row[0])
                line_count += 1
    return csv_reader

def main():
    """Main Function to read in the
        users values
    """
    items = read_in_values()
    print(items)
    num_circ = input("Num Of Circuits: ")
    print("1: LV 2: MV 3: HV 4: EV 5: IV")
    lvl_circ = input("Level Of Circuits: ")
    print("1: Basic 2: Good 3: Plastic 4: Advanced")
    curr_lvl = input("Board To Use: ")
    print("1: LV 2: MV 3: HV 4: EV 5: IV")
    lvl_mach= input("Level Of Machine: ")


if __name__ == "__main__":
    main()
