import os
import sys
import datetime
import pandas as pd


def ceil_dt(dt):
    #how many secs have passed this hour
    nsecs = dt.minute * 60 + dt.second + dt.microsecond * 1e-6
    #number of seconds to next quarter hour mark
    #Non-analytic (brute force is fun) way:
    #   delta = next(x for x in xrange(0,3601,900) if x>=nsecs) - nsecs
    #anlytic (ARGV BATMAN!, what is going on with that expression) way:
    delta = (nsecs // 900) * 900 + 900 - nsecs
    #time + number of seconds to quarter hour mark.
    return dt + datetime.timedelta(seconds=delta)


def get_data(now):
    file_today = '{}{:02d}{:02d}'.format(now.year, now.month, now.day)
    filename = os.path.expanduser('~/Documents/timesheets/{}.csv'.format(file_today))
    if os.path.isfile(filename):
        data = pd.read_csv(filename, parse_dates=True, index_col=0)
    else:
        today = '{}/{}/{}'.format(now.month, now.day, now.year)
        rng = pd.date_range(today, periods=24, freq='H')

        ts = pd.DataFrame(columns=['type', 'action'], index=rng)
        data = ts.asfreq('15Min', method='pad')

    return data, filename


def main():
    action = sys.argv[1]
    type_class = sys.argv[2]

    now = datetime.datetime.now()
    data, filename = get_data(now)

    entry_time = ceil_dt(now)

    data.loc[entry_time, 'action'] = action
    data.loc[entry_time, 'type'] = type_class
    data.to_csv(filename)


if __name__ == '__main__':
    main()
