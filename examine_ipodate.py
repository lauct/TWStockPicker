# -*- coding: UTF-8 -*-
import urllib2
from datetime import datetime
import sys
from readcsv import readcsv
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding('UTF-8')

stock_id_dict = readcsv()

def examine_ipodate(stocks_array):
    # stocks_array = stocks.split("\n")
    stocks_to_remove_array = []
    print stocks_array

    for x in stocks_array:
        if x.startswith("00"): # delete ETF
            print "ETF: "+ x
            stocks_array.remove(x)
        if int(x)>=10000: # delete 可轉換公司債
            stocks_to_remove_array.append(str(x))

    for x in stocks_to_remove_array:
        stocks_array.remove(x)

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

        soup = BeautifulSoup(html, "html.parser")

        # IPOdate
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

    return 0

print stock_id_dict['TWSE_ID_LIST']
print stock_id_dict['GTSM_ID_LIST']

examine_ipodate(stock_id_dict['TWSE_ID_LIST'])
examine_ipodate(stock_id_dict['GTSM_ID_LIST'])
