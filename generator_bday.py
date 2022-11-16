import datetime


def get_holiday():
    """
    예저로 실제의 경우에는 api나 휴일 데이터베이스를 연동하여 사용
    :return: list()
    """
    return [datetime.datetime(2022, 8, 31).date()]


def business_date_generator(today: datetime.datetime(), business_days: int):
    """

    :param today:
    :param business_days:
    :return:
    """
    index_date = today
    holiday_list = get_holiday()
    while business_days > 0:
        if not index_date.weekday() > 4 and index_date.date() not in holiday_list:
            business_days -= 1
            yield index_date
        index_date = index_date + datetime.timedelta(days=1)


for business_date in business_date_generator(datetime.datetime.today(), 10):
    print(business_date)
