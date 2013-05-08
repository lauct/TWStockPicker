# -*- coding: UTF-8 -*-
import urllib2
from datetime import datetime
from bs4 import BeautifulSoup
import csv
import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

stocks = """3658
1565
8406
3131
4966
3691
4152
8299"""
# 3582
# 2729
# 2926
# 24612
# 4994
# 6130
# 30542
# 23952
# 5274
# 3176
# 6803
# 4162
# 32901
# 32361
# 14774
# 34901
# 5536
# 8044
# 5903
# 33901
# 1558
# 4416
# 68031
# 20592
# 4933
# 3611
# 4965
# 25372
# 25281
# 30603
# 62062
# 32605
# 6121
# 99451
# 15043
# 36981
# 25374
# 35512
# 25373
# 1580
# 24422
# 4168
# 5306
# 62613
# 4947
# 99411
# 61153
# 53923
# 25362
# 17203"""
stocks_array = stocks.split("\n")
stocks_to_remove = []
print stocks_array

for x in stocks_array:
    if x.startswith("00"): # delete ETF
        print x
        stocks_array.remove(x)
    if int(x)>=10000: # delete 可轉換公司債
        stocks_to_remove.append(str(x))
for x in stocks_to_remove:
    stocks_array.remove(x)
print stocks_array

stock_examined_id = []
stock_examined_shortname = []
stock_failed_id = []
stock_failed_shortname = []
stock_pair_passed_list = {}
stock_pair_failed_list = {}
ON_MARKET = "ctl00_ContentPlaceHolder1_Label018"
ON_BOX = "ctl00_ContentPlaceHolder1_Label042"
SHORT_NAME = "ctl00_ContentPlaceHolder1_Label001"

for stock_id in stocks_array:
    stock_url = 'http://www.cnyes.com/twstock/intro/' + stock_id + '.htm'
    response = urllib2.urlopen(stock_url)
    html = response.read()

    soup = BeautifulSoup(html)

    # IPOdate
    # print "IPO"
    IPODateString = ""
    if len(soup.find("span", {"id": ON_MARKET}).text) > 0:
        IPODateString = soup.find("span", {"id": ON_MARKET}).text
    else:
        IPODateString = soup.find("span", {"id": ON_BOX}).text
    stock_short_name = soup.find("span", {"id": SHORT_NAME}).text

    if "/" in IPODateString:
        IPODateStringArray = IPODateString.split('/')
        YearOfIPODateRawInt = int(IPODateStringArray[0])
        if YearOfIPODateRawInt < 1000:
            YearOfIPODateInAD = YearOfIPODateRawInt + 1911
            MonthOfIPODateInAD = IPODateStringArray[1]
            DayOfIPODateInAD = IPODateStringArray[2]
            IPODateInAD = str(YearOfIPODateInAD) + MonthOfIPODateInAD + DayOfIPODateInAD
            IPODate = datetime.strptime(IPODateInAD, '%Y%m%d')
        else:
            YearOfIPODateInAD = YearOfIPODateRawInt
            MonthOfIPODateInAD = IPODateStringArray[1]
            DayOfIPODateInAD = IPODateStringArray[2]
            IPODateInAD = YearOfIPODateInAD + MonthOfIPODateInAD + DayOfIPODateInAD
            IPODate = datetime.strptime(str(IPODateInAD), '%Y%m%d')
    else:
        IPODate = datetime.strptime(IPODateString, '%Y%m%d')

    now = datetime.now()
    DaysSinceIPO = now - IPODate
    stock_pass = False

    if DaysSinceIPO.days >= 365*2:
        stock_pass = True



    print stock_short_name + u'已上市' + str(DaysSinceIPO.days)+ u'天'
    print u'上市日期：' + str(IPODate.year) + "-" + str(IPODate.month) + "-" + str(IPODate.day)
    if stock_pass:
        stock_examined_id.append(stock_id)
        stock_examined_shortname.append(stock_short_name)
        stock_pair_passed_list[stock_id] = stock_short_name
        print u'✅\t通過\n'
    else:
        stock_failed_id.append(stock_id)
        stock_failed_shortname.append(stock_short_name)
        stock_pair_failed_list[stock_id] = stock_short_name

        print u'❌\t未滿兩年\n'

for name in stock_examined_shortname:
    if "F-" in name:
        print name

for x in stock_examined_id:
    print "PASS: " + x + "\t" + stock_pair_passed_list[x]
for x in stock_failed_id:
    print "FAIL: " + x + "\t" + stock_pair_failed_list[x]

data = [  
  [' 101/01/31', '5,486,734,180', '162,361,181,834', '1,283,951', '7,517.08', '109.67'],  
  [' 101/01/13', '3,497,838,901', '99,286,437,370', '819,762', '7,181.54', '-5.04'],  
]  
f = open("stock.csv","w")  
w = csv.writer(f)  
w.writerows(data)  
f.close()      