from datetime import datetime, timedelta

def compute_prev_date(dates_list: list):
    prev_days_list = []
    fmt = '%Y-%m-%d'
    prev_date_format = '%d %b %Y'
    for date in dates_list:
        prev_date = datetime.strptime(date, fmt) - timedelta(1)
        formarted_prev_day = prev_date.strftime(prev_date_format)
        prev_days_list.append(formarted_prev_day)
    return prev_days_list

if __name__ == '__main__':
    list = compute_prev_date(["1999-01-21", "2012-12-30"])
    print(list)
