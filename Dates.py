from datetime import datetime

def is_date_format_correct(date: str) -> bool:
    """
    This function takes in a date in string format
    and returns true if the date matches the format
    YYYY-MM-DD and false if it doesn't
    """
    date_format = '%Y-%m-%d'
    try:
        datetime.strptime(date, date_format)
        return True
    except ValueError:
        return False

if __name__ == '__main__':
    boool = is_date_format_correct('2000-09-28')
    print(boool)
