from katalyma import Katalyma
from global_vars import *


def get_slew(new_date):
    katalyma_now = Katalyma(filename=FILENAME, cycle=CYCLE)
    error = katalyma_now.get_errors()
    if error:
        return error
    katalyma_now.provide_next(new_date)
    katalyma_now.perform_checks()
    error = katalyma_now.get_errors()
    if error:
        return error
    katalyma_now.write_in()
    return "So far, so good"


def get_unslew():
    katalyma_now = Katalyma(filename=FILENAME, cycle=CYCLE)
    katalyma_now.provide_prev()
    katalyma_now.perform_checks()
    error = katalyma_now.get_errors()
    if error:
        return error
    katalyma_now.write_in()
    return "So far, so good"


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
        return "So far, so good"


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


if __name__ == '__main__':
    pass
    # 26.12.2017
    # 2
    # gray - black
    # 19.12.2017

    print(rewrite_file("19.12.2017 3 12.12.2017"))
    # print(rewrite_file("19.12.2017 3"))
    # print(get_slew("26.12.2017"))
    # print(get_unslew())
    # print(see_curr())
    # print(see_next())





