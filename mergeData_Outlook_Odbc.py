# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:41:49 2019

@author: A

This is an example python code for demostration
This example code picks up data from sample database via odbc and
from outlook (reading emails)
"""

import sql_queries as q
import readLast6emailsFilterBySubject as email6
import pandas as pd
import pyodbc

################ --> SOURCE: Direct BEAT ODBC
connOdbc = pyodbc.connect('DSN=ODBC64')
################ --> SOURCE: Direct BEAT ODBC

# let's get the data
dfK = pd.read_sql(q.sqlK, connOdbc)
print("*****DATA K ****************************************\n" + str(dfK))

dfA = pd.read_sql(q.sqlA, connOdbc)
print("\n\n*****DATA A *********************************\n" + str(dfA))

dfI = pd.read_sql(q.sqlI, connOdbc)
print("\n\n*****DATA I ******************************\n" + str(dfI))

dfD = pd.read_sql(q.sqlD, connOdbc)
print("\n\n*****DATA D *********************************\n" + str(dfD))

dfDLastMonth = pd.read_sql(q.sqlDLastMonth, connOdbc)
print("\n\n*****DATA D Last Month***********************\n" + str(dfDLastMonth))

dfEmails = email6.getIDsFromEmails()
print("\n\n*****IDs From Emails *****************\n" + str(dfEmails))

print("\n\n")
print("1 bussiness day ago: " + str(q.ago1BussDay))
print("3 bussiness days ago: " + str(q.ago3BussDays))
print("1 bussiness month ago: " + str(q.ago1BussMonth))
print("First day of current month: " + str(q.firstDayCurrMonth))
print("First day of last month: " + str(q.firstDayLastMonth))
print("Last day of last month: " + str(q.lastDayLastMonth))
print("30 ordinary days ago: " + str(q.ago30OrdDays))
