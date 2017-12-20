from global_vars import *
from process_input import process_date


class Katalyma(object):

    def __init__(self, filename, cycle, curr_date=None, curr_ind=None, curr_content=None, prev_date=UNKNOWN):
        self._filename = filename
        self._cycle = cycle
        self._curr_date = curr_date
        self._curr_ind = curr_ind
        self._curr_content = curr_content
        self._prev_date = prev_date
        self._new_date = None
        self._new_ind = None
        self._new_content = None

        if self._curr_ind is None: self.read_out()
        else: self.write_in()

    def write_in(self):
        with open(self._filename, 'w') as handler:
            handler.write(self._new_date + '\n')
            handler.write(str(self._new_ind) + '\n')
            handler.write(self._new_content + '\n')
            handler.write(self._curr_date)
        return True

    def read_out(self):
        with open(self._filename) as handler:
            self._curr_date = handler.readline()
            self._curr_ind = int(handler.readline())
            self._curr_content = handler.readline()
            self._prev_date = handler.readline()

    def plug_new_date(self, new_date):
        self._new_date = new_date

    def provide_next(self, new_date):
        self._prev_date = self._curr_date
        self._new_date = new_date
        self._new_ind = (self._curr_ind + 1) % len(self._cycle)
        self._new_content = str(self._cycle[self._new_ind])

    def provide_prev(self):
        self._new_date = self._curr_date = self._prev_date
        self._new_ind = self._curr_ind = (self._curr_ind - 1) % len(self._cycle)
        self._new_content = self._curr_content = str(self._cycle[self._curr_ind])
        self._prev_date = UNKNOWN

    def perform_checks(self):
        pass


if __name__ == '__main__':
    pass


