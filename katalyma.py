from global_vars import *
from process_data import *


class Katalyma(object):

    def __init__(self, filename, cycle, curr_date=None, curr_ind=None, prev_date=UNKNOWN, new_there=False):
        self._error = None
        self._filename = filename
        self._cycle = cycle
        self._curr_date = string_to_date(curr_date)
        self._curr_ind = process_int(curr_ind)
        self._curr_content = None
        self._prev_date = string_to_date(prev_date)
        self._new_there = new_there

        self.fill_in_curr_content()

        if new_there:
            if not self._prev_date:
                self._prev_date = UNKNOWN
            self._error = self.perform_checks()
            if not self._error:
                self.write_in()
        else:
            self.read_out()
            if not self._prev_date:
                self._prev_date = UNKNOWN
            self._error = self.perform_checks()

    def get_curr(self):
        if self._prev_date == UNKNOWN:
            prev_date = UNKNOWN
        else:
            prev_date = date_to_string(self._prev_date)
        return "Date: %s\nIndex: %d\n%s\nPrevious date: %s" % (date_to_string(self._curr_date),
                                                               self._curr_ind,
                                                               tuple_to_string(self._curr_content),
                                                               prev_date)

    def perform_checks(self):
        try:
            handler = open(self._filename)
        except FileNotFoundError:
            return 1
        handler.close()

        if not (type(self._curr_date) is datetime or self._curr_date == UNKNOWN):
            return 2

        if type(self._curr_ind) is not int:
            return 3

        if type(self._curr_content) is not tuple:
            return 4

        if not (type(self._prev_date) is datetime or self._prev_date == UNKNOWN):
            return 5

    def get_errors(self):
        try:
            return ERRORS[self._error]
        except KeyError:
            return

    def write_in(self):
        with open(self._filename, 'w') as handler:
            handler.write(date_to_string(self._curr_date) + '\n')
            handler.write(str(self._curr_ind) + '\n')
            handler.write(tuple_to_string(self._curr_content) + '\n')
            handler.write(date_to_string(self._prev_date))
        return True

    def read_out(self):
        with open(self._filename) as handler:
            self._curr_date = string_to_date(handler.readline().strip())
            self._curr_ind = process_int(handler.readline().strip())
            self.fill_in_curr_content()
            handler.readline()
            self._prev_date = string_to_date(handler.readline().strip())

    def fill_in_curr_content(self):
        try:
            self._curr_content = self._cycle[self._curr_ind]
        except (IndexError, TypeError):
            self._curr_content = None

    def provide_next(self, new_date):
        self._new_there = True
        self._prev_date = self._curr_date
        self._curr_date = string_to_date(new_date)
        self._curr_ind = (self._curr_ind + 1) % len(self._cycle)
        self.fill_in_curr_content()

    def provide_prev(self):
        self._curr_date = self._prev_date
        self._curr_ind = (self._curr_ind - 1) % len(self._cycle)
        self.fill_in_curr_content()
        self._prev_date = UNKNOWN


if __name__ == '__main__':
    pass
