import datetime


class workDays:
    def __init__(self, start_date, end_start, days_off=None):
        """
        weekday()方法将一个日期转换对应成星期，以星期一（0）到星期天（6）结束
        :param start_date: 开始时间,必须是datetime格式
        :param end_start: 结束时间,必须是datetime格式
        :param days_off: 休息日，默认为周六周日
        """
        self.start_date = start_date
        self.end_date = end_start
        self.days_off = days_off

        if self.start_date > self.end_date:  # 防止开始日期和结束日期传入反了
            self.start_date, self.end_date = self.end_date, self.start_date

        if self.days_off is None:  # 休息日为周六、周日
            self.days_off = 5, 6
        # 每周工作日列表
        self.days_work = [i for i in range(7) if i not in self.days_off]

    def workDays(self):  # 计算出自定义范围内有多少个工作日，包含节假日
        tag_date = self.start_date
        while True:
            if tag_date > self.end_date:
                break

            if tag_date.weekday() in self.days_work:  # 判断日期为非周末
                yield tag_date

            tag_date += datetime.timedelta(days=1)

    def holiday(self):  # 计算自定义范围内节假日占多少
        holiday = "20210101,20210211,20210212,20210215,20210216,20210217,20210405,20210503,20210504,20210505,20210614,20210920,20210921,20211001,20211004,20211005,20211006,20211007"
        holidayList = holiday.split(",")
        for i in holidayList:
            date = datetime.datetime(int(i[0:4]), int(i[4:6]), int(i[6:8]))
            if self.start_date < date < self.end_date:  # 判断节假日在自定义的范围内
                if date.weekday() in self.days_work:  # 判断为非非周末
                    yield date

    def daysCount(self):  # 计算工作日，不包含节假日
        return len(list(self.workDays()))-len(list(self.holiday()))

