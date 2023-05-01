import sys
sys.path.append('./lunar-python')

from lunar_python import Lunar, Solar
from lunar_python.util import HolidayUtil
from datetime import datetime
import functools

dateStart = Lunar.fromYmd(2023, 8, 17)
dateEnd = Lunar.fromYmd(2024, 1, 1)

def IsMarryYi(date):
	return '嫁娶' in date.getDayYi()

def IsMarryJi(date):
	return '嫁娶' in date.getDayJi()

def isWork(date):
	work = True
	solar = date.getSolar()
	holiday = HolidayUtil.getHoliday(solar.getYear(), solar.getMonth(), solar.getDay())
	if holiday is None:
		week = solar.getWeek()
		if 0 == week or 6 == week:
			work = False
	else:
		work = holiday.isWork()
	return work

def eqDate(date1, date2):
       return date1.toString() == date2.toString();

dateCur = dateStart;
dates = [dateCur];
while not eqDate(dateCur,dateEnd):
	dateCur = dateCur.next(1)
	dates.append(dateCur)

filters = [
	IsMarryYi, 
	lambda x: not isWork(x)
	]
filterFunc = functools.reduce(lambda f, g: lambda x: f(x) and g(x), filters)

filtered_list = list(filter(filterFunc, dates))

for date in filtered_list:
	# print(date.getSolar().toFullString())
	print(date.getSolar().toYmd())
	