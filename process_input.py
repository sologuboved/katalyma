from datetime import datetime
DOT = '.'

# strftime("%d %B %Y, %A %H:%M:%S")


def process_date(raw_date):
    if raw_date == 'today':
        return datetime.today()

    try:
        date = list(map(int, map(lambda i: i.strip(), raw_date.split(DOT))))
    except ValueError:
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


def process_int(raw_int):
    try:
        return int(raw_int)
    except ValueError:
        return


def process_content(raw_content):
    return raw_content


if __name__ == '__main__':
    print(process_date(""))

