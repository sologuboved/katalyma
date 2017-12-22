from katalyma import Katalyma
from global_vars import *


def slew(new_date):
    katalyma_now = Katalyma(filename=FILENAME, cycle=CYCLE)
    katalyma_now.provide_next(new_date)
    katalyma_now.perform_checks()
    error = katalyma_now.get_errors()
    if error:
        return error
    katalyma_now.write_in()
    return "So far, so good"


def unslew():
    katalyma_now = Katalyma(filename=FILENAME, cycle=CYCLE)
    katalyma_now.provide_prev()
    katalyma_now.perform_checks()
    error = katalyma_now.get_errors()
    if error:
        return error
    katalyma_now.write_in()
    return "So far, so good"


def rewrite_file(curr_date, curr_ind, prev_date=None):
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


def get_out():
    katalyma_now = Katalyma(filename=FILENAME, cycle=CYCLE)
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

    # print(rewrite_file("19.12.2017", '3'))
    # print(rewrite_file("19.12.2017", '3'))
    # print(slew("26.12.2017"))
    print(unslew())




