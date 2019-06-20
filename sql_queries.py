# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:27:15 2019

@author: A
"""

import pandas as pd
import datetime
import dateutil.relativedelta
import calendar as cal
from workalendar.europe import Sweden


calWorkDays = Sweden()
now = datetime.datetime.now().date()
# First day of the current month
firstDayCurrMonth = now.replace(day=1)
# First day of last month
firstDayLastMonth = firstDayCurrMonth + dateutil.relativedelta.relativedelta(months=-1)
# Last day of last month
lastDayLastMonth = firstDayCurrMonth - datetime.timedelta(days=1)
# 1 days ago
ago1BussDay = calWorkDays.sub_working_days(now, 1)
# 3 days ago
ago3BussDays = calWorkDays.sub_working_days(now, 3)
# 1 month ago
exactDay1MonthAgo = now + dateutil.relativedelta.relativedelta(months=-1)
ago1BussMonth = exactDay1MonthAgo
ago30OrdDays = now + dateutil.relativedelta.relativedelta(days = -30)
# print(ago1BussMonth)
while not calWorkDays.is_working_day(ago1BussMonth):
    ago1BussMonth = calWorkDays.sub_working_days(ago1BussMonth, 1)
    # print("ago1BussMonth: " + str(ago1BussMonth))


# These are example queries. Replace them with yours
sqlK = '''SELECT *
FROM tableK tk
WHERE ( tk.DAY = TO_DATE(\'''' + str(ago1BussDay) + '''\', 'YYYY-MM-DD') )
GROUP BY 1,2;'''

sqlA = '''Select *
from (SELECT *
FROM tableA ta
WHERE ( ta.DAY = TO_DATE(\'''' + str(ago1BussDay) + '''\', 'YYYY-MM-DD') )
GROUP BY 3
HAVING ( ( SUM(column) ) > '0' ) ) t;'''

sqlI = '''Select *
from tableI ti
WHERE ( DAY BETWEEN TO_DATE(\'''' + str(ago30OrdDays) + '''\', 'YYYY-MM-DD') AND TO_DATE(\'''' + str(ago3BussDays) + '''\', 'YYYY-MM-DD') )
ORDER BY DAY DESC;'''

sqlD = '''Select *
FROM tableD td
WHERE ( DAY BETWEEN  TO_DATE(\'''' + str(firstDayCurrMonth) + '''\', 'YYYY-MM-DD')  AND  TO_DATE(\'''' + str(ago1BussDay) + '''\', 'YYYY-MM-DD')  ) ;'''

sqlDLastMonth = '''Select *
FROM tableDL tdl
WHERE ( DAY BETWEEN  TO_DATE(\'''' + str(firstDayLastMonth) + '''\', 'YYYY-MM-DD')  AND  TO_DATE(\'''' + str(lastDayLastMonth) + '''\', 'YYYY-MM-DD')  );'''