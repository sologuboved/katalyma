from katalyma import Katalyma
from global_vars import *
from process_data import tuple_to_string, process_int


def get_slew(new_date):
    katalyma_now = Katalyma(filename=FILENAME, cycle=CYCLE)
    error = katalyma_now.get_errors()
    if error:
        return error
    if not new_date:
        new_date = 'today'
    katalyma_now.provide_next(new_date)
    katalyma_now.perform_checks()
    error = katalyma_now.get_errors()
    if error:
        return error
    katalyma_now.write_in()
    return ALRIGHT


def get_unslew():
    katalyma_now = Katalyma(filename=FILENAME, cycle=CYCLE)
    katalyma_now.provide_prev()
    katalyma_now.perform_checks()
    error = katalyma_now.get_errors()
    if error:
        return error
    katalyma_now.write_in()
    return ALRIGHT


def rewrite_file(user_input):
    try:
        curr_date, curr_ind = user_input.split()
        prev_date = UNKNOWN
    except ValueError:
        try:
            curr_date, curr_ind, prev_date = user_input.split()
        except ValueError:
            curr_date = user_input
            curr_ind = None
            prev_date = None
    katalyma_now = Katalyma(filename=FILENAME,
                            cycle=CYCLE,
                            curr_date=curr_date,
                            curr_ind=curr_ind,
                            prev_date=prev_date,
                            new_there=True)
    katalyma_now.perform_checks()
    error = katalyma_now.get_errors()
    if error:
        return error
    else:
        return ALRIGHT


def see_curr():
    katalyma_now = Katalyma(filename=FILENAME, cycle=CYCLE)
    katalyma_now.perform_checks()
    error = katalyma_now.get_errors()
    if error:
        return error
    else:
        return katalyma_now.get_curr()


def see_next():
    katalyma_now = Katalyma(filename=FILENAME, cycle=CYCLE)
    katalyma_now.provide_next(UNKNOWN)
    katalyma_now.perform_checks()
    error = katalyma_now.get_errors()
    if error:
        return error
    else:
        return katalyma_now.get_curr()


def see_cycle(user_input):
    if user_input:
        ind = process_int(user_input)
        try:
            return tuple_to_string(CYCLE[ind])
        except (IndexError, TypeError):
            return INVALID_INPUT
    cycle = ''
    for ind in range(len(CYCLE)):
        cycle += "%d: %s\n" % (ind, tuple_to_string(CYCLE[ind]))
    return cycle
