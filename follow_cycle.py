from global_vars import *
from process_date_input import process_date

FILENAME = 'updates.txt'
INVALID_INPUT = "Invalid input!"
WRONG = "Something is wrong with the file"
SUCCESS = "Written in"
LEN_CYCLE = 12


def write_in(date, cycle_ind, cycle_content):
    with open(FILENAME, 'w') as handler:
        handler.write(str(date) + '\n')
        handler.write(str(cycle_ind) + '\n')
        handler.write(str(cycle_content) + '\n')
    return True


def read_out():
    with open(FILENAME) as handler:
        date = handler.readline()
        cycle_ind = handler.readline()
        cycle_content = handler.readline()
    return date, cycle_ind, cycle_content


def slew(raw_date):
    new_date = process_date(raw_date).strftime('%d.%m.%Y')
    print(new_date)
    if not new_date:
        return INVALID_INPUT
    try:
        previous_date, previous_ind, previous_content = map(lambda item: item.strip(), read_out())
    except ValueError:
        return WRONG
    new_ind = (int(previous_ind) + 1) % LEN_CYCLE
    new_content = CYCLE[new_ind]
    if write_in(new_date, new_ind, new_content):
        print(SUCCESS)
    return new_date, new_ind, new_content


def unslew():
    pass


if __name__ == '__main__':
    print(slew('today'))
