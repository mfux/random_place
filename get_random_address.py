from random import randint
ADDR_FILE = "data/addresses.json"
N_LINES= 8584

line_nr = randint(0, N_LINES-1)
with open(ADDR_FILE, 'r') as fp:
    for i, line in enumerate(fp):
        if i == line_nr:
            street, nr, plz = line.split(";")
            print(street, nr, plz)
            break
