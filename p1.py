import datetime
import time
from io import StringIO
import pandas


def diff_days(csv_contents: str) -> int:
    # Given a the contents of a CSV file as csv_contents, return the difference in days between the date of the earliest and the oldest entry. The CSV file starts with a header row, which contains at least one column called Date.

    # Parse the CSV file as a Pandas DataFrame.
    df = pandas.read_csv(StringIO(csv_contents))

    # Convert the Date column of the parsed data to python datetime type.
    dates = df["Date"].tolist()
    dates = list(map(lambda x: datetime.datetime(*time.strptime(x, "%Y-%m-%d")[0:6]), dates))

    # Find the minimum and the maximum dates of the Date column.
    diff = max(dates) - min(dates)

    return diff.days

print(diff_days('Date\n6427-01-01\n2000-01-01\n'))