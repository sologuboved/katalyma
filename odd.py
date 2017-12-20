def write_in(filename, date, cycle_ind, cycle_content, prev_date):
    with open(filename, 'w') as handler:
        handler.write(str(date) + '\n')
        handler.write(str(cycle_ind) + '\n')
        handler.write(str(cycle_content) + '\n')
        handler.write(str(prev_date) + '\n')
    return True


def read_out(filename):
    with open(filename) as handler:
        curr_date = handler.readline()
        cycle_ind = handler.readline()
        cycle_content = handler.readline()
        prev_date = handler.readline()
    return curr_date, cycle_ind, cycle_content, prev_date

