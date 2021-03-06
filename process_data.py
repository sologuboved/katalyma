from datetime import datetime
from global_vars import UNKNOWN
DOT = '.'


def tuple_to_string(raw_tuple):
    return "%s - %s" % (raw_tuple[0], raw_tuple[1])


def date_to_string(cooked_date):
    if cooked_date == UNKNOWN:
        return UNKNOWN
    try:
        return cooked_date.strftime("%d.%m.%Y")
    except AttributeError:
        return


def string_to_date(raw_date):
    if raw_date == UNKNOWN:
        return UNKNOWN

    if raw_date == 'today':
        return datetime.today()

    try:
        date = list(map(int, map(lambda i: i.strip(), raw_date.split(DOT))))
    except (ValueError, AttributeError):
        return

    date.reverse()
    length = len(date)

    if not length or length > 3:
        return

    if length == 3:
        try:
            return datetime(*date)
        except (TypeError, ValueError):
            return

    this_year = datetime.today().year

    if length == 1:
        this_month = datetime.today().month
        try:
            return datetime(this_year, this_month, *date)
        except (TypeError, ValueError):
            return

    try:
        return datetime(this_year, *date)
    except (TypeError, ValueError):
        return


def tuple_to_str(tpl):
    return tpl[0] + " - " + tpl[1]


def process_int(raw_int):
    try:
        return int(raw_int)
    except (ValueError, TypeError):
        return
