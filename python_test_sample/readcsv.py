# -*- coding: UTF-8 -*-

__author__ = 'chun'

import csv

stock_id_list = []
csv_file_list = ['TWSE_price_ranking.csv', 'GTSM_price_ranking.csv']

for filename in csv_file_list:
    with open(filename, 'rb') as csvfile:
        twsereader = csv.DictReader(csvfile, ['代碼', '名稱', '成交'])
        print "----------------------------------"
        for row in twsereader:
            if row['代碼'] == '代碼':
                pass
            else:
                print row['代碼']
        print "----------------------------------"

    csvfile.close()