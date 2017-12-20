from katalyma import Katalyma
from process_input import process_date, process_int, process_content
from global_vars import *


def slew(raw_date):
    new_date = process_date(raw_date).strftime('%d.%m.%Y')
    katalyma_now = Katalyma(filename=FILENAME, cycle=CYCLE)
    katalyma_now.provide_next(new_date)
    katalyma_now.write_in()


def unslew():
    katalyma_now = Katalyma(filename=FILENAME, cycle=CYCLE)
    katalyma_now.provide_prev()
    katalyma_now.write_in()


def fill_in(curr_date, curr_ind, curr_content, prev_date):
    curr_date = process_date(curr_date).strftime('%d.%m.%Y')
    curr_ind = process_int(curr_ind)
    curr_content = process_content(curr_content)
    prev_date = process_date(curr_date).strftime('%d.%m.%Y')
    Katalyma(filename=FILENAME,
             cycle=CYCLE,
             curr_date=curr_date,
             curr_ind=curr_ind,
             curr_content=curr_content,
             prev_date=prev_date)


if __name__ == '__main__':
    pass
