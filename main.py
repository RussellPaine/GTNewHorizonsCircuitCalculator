"""Simple program to figure out the
    best and easiest circuit to make
"""
import csv

#TODO add in a split path for selecting circuit from the get go

class Node():
    """A node for the crafting tree created
        by the csv values
    """
    # pylint: disable=too-many-instance-attributes
    def __init__(self, _n, _i1, _i2, _i3, _i4, _i5, _i6, _i7, _i8, _i9, _n1, _n2, _n3, _n4, _n5, _n6, _n7, _n8, _n9, _machine, _produce, _level, _tier):
        """Intilises the Node object
        """
        self.name = _n
        self.i_1 = _i1
        self.i_2 = _i2
        self.i_3 = _i3
        self.i_4 = _i4
        self.i_5 = _i5
        self.i_6 = _i6
        self.i_7 = _i7
        self.i_8 = _i8
        self.i_9 = _i9
        self.n_1 = _n1
        self.n_2 = _n2
        self.n_3 = _n3
        self.n_4 = _n4
        self.n_5 = _n5
        self.n_6 = _n6
        self.n_7 = _n7
        self.n_8 = _n8
        self.n_9 = _n9
        self.machine = _machine
        self.produce = _produce
        self.level = _level
        self.tier = _tier

    def get_crafting_grid(self):
        """Returns the items and the amount for crafting
        """
        return [[self.i_1, self.n_1], [self.i_2, self.n_2], [self.i_3, self.n_3], [self.i_4, self.n_4], [self.i_5, self.n_5], [self.i_6, self.n_6], [self.i_7, self.n_7], [self.i_8, self.n_8], [self.i_9, self.n_9]]

def read_in_values():
    """Reads in items from CSV
    """
    structure = {}
    csv_reader = 0
    with open('items.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count != 0:
                structure[int(row[0])] = Node(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17], row[18], row[19], row[20], row[21], row[22], row[23])
            line_count += 1
    return structure

def get_circuits(items):
    circuit_id_list = []
    for i in items:
        if items[i].level == '1':
            circuit_id_list.append(i)
    return circuit_id_list

def get_user_input():
    num_circ = input("Num Of Circuits: ")
    print("1: LV 2: MV 3: HV 4: EV 5: IV")
    lvl_mach = input("Level Of Machine: ")
    print("1: Basic 2: Good 3: Plastic 4: Advanced 5: Frame")
    lvl_board = input("Board To Use: ")
    
    return num_circ, lvl_board, lvl_mach

def find_valid_circuits(lvl_board, lvl_mach, circuit_id_list, items):
    valid_circuit_list = []

    board_list = {
        1: '14',
        2: '19',
        3: '37',
        4: '50',
        5: '47'
    }
    for circuit in circuit_id_list:
        if int(lvl_mach) >= int(items[circuit].tier) and int(board_list[int(lvl_board)]) == int(items[circuit].i_1):
            valid_circuit_list.append(circuit)
    return valid_circuit_list

def confirm_circuit(valid_circuit_list, items):
    print("Which Circuit Would You Like To Make?")
    for i, circ in enumerate(valid_circuit_list):
        print(str(i +1) + ": " + items[circ].name)
    circuit_id = input("Level Of Machine: ")

    return valid_circuit_list[int(circuit_id) - 1]

def get_number_of_item(num_circ, circuit_id, items):
    outlist = []
    comps = items[circuit_id].get_crafting_grid()
    for comp in comps:
        if comp[0] == 'NULL':
            continue
        poss = comp[0].split('|')
        choice = 0
        if len(poss) > 1:
            print("Which component to use?")
            for i, p in enumerate(poss):
                print(str(i + 1) + ": " + items[int(p)].name)
            temp = input()
            choice = int(temp) - 1
        amount = comp[1].split('|')
        outlist.append(items[int(poss[choice])].name + ": " +  str(int(amount[choice]) * int(num_circ)))
    return outlist

def main():
    """Main Function to read in the
        users values
    """
    items = read_in_values()
    circuit_id_list = get_circuits(items)
    num_circ, lvl_board, lvl_mach = get_user_input()
    valid_circuit_list = find_valid_circuits(lvl_board, lvl_mach, circuit_id_list, items)
    circuit_id = confirm_circuit(valid_circuit_list, items)
    list_comps = get_number_of_item(num_circ, circuit_id, items)
    print("Your Shopping List:")
    for component in list_comps:
        print(component)


if __name__ == "__main__":
    main()
