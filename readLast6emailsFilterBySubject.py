# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:20:38 2019

@author: A
"""

import win32com.client
import sys
import pandas as pd
import numpy as np
import datetime
import dateutil.relativedelta
# import unicodecsv as csv
if sys.version_info[0] < 3:
    from StringIO import StringIO
else:
    from io import StringIO

######################
def getCharsFromSubToEnd(text, sub1):
    pos1 = text.lower().find(sub1.lower()) + len(sub1)
    return text[pos1:]
######################
# -->Solution to NaN valued ID column
# Drop NaN valued cells to the left
def squeeze_nan(x, hold):
    if x.name not in hold:
        original_columns = x.index.tolist()
        squeezed = x.dropna()
        squeezed.index = [original_columns[n] for n in range(squeezed.count())]
        return squeezed.reindex(original_columns, fill_value=np.nan)
    else:
        return x
# <--Solution to NaN valued ID column
########################


def getIDsFromEmails(mySubject, lastLineBeforeData):
    
    # mySubject = "SUBJECT"
    # lastLineBeforeData = "C1 C2           C3\r\n\r\n"
    
    now = datetime.datetime.now().date()
    # ago6days: this example filters the emails which with receiving date.
    # you can replace 6 with your selection
    ago6days = now + dateutil.relativedelta.relativedelta(days=-6)

    # Replace your column names with 'ColumnA','ColumnB'
    dfID = pd.DataFrame(columns=['ColumnA', 'ColumnB'])

    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # "6" refers to the index of a folder
                                        # - in this case,the inbox. 
    messages = inbox.Items
    messages.Sort("[ReceivedTime]", False)
    
    for i, message in enumerate(messages):  # enumerated the items
        try:
            subject = message.subject

            # Replace your own subject with "SUBJECT"
            if mySubject in subject:
                if message.ReceivedTime.date() >= ago6days:
                    MessageBody = message.body
                    # print(message.ReceivedTime.date())
                    # Get text after subStart from the email. You should 
                    # replace the value of subStart
                    subStart = lastLineBeforeData
                    subString = getCharsFromSubToEnd(MessageBody, subStart)
                    subString = StringIO(subString)
                    df = pd.read_csv(subString, sep="  ", header=None, engine='python')

                    # -->Solution to NaN valued ID column
                    df.apply(lambda x: squeeze_nan(x, ['WhatEverYouWant']), axis=1)
                    # print("==> df :" + str(df))
                    try:
                       val = int(df.index[0])
                    except ValueError:
                       df = pd.DataFrame(df.index)
                    # <-- Solution to NaN valued ID column

                    # Get the right ID
                    # dfID = df[0].str[5:]
                    # Replace your column names with 'ColumnA','ColumnB'
                    df[['remove', 'ColumnA']] = df[0].str.split(" ", 1, expand=True)
                    df['ColumnB'] = message.ReceivedTime.date()

                    dfID = dfID.append(pd.DataFrame(df[['ColumnA', 'ColumnB']]))
                    # print(dfID)
        except Exception as e:
            ()  # print(e.__cause__)

#    return pd.DataFrame(dfID)
    return dfID

