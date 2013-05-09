# -*- coding: UTF-8 -*-

__author__ = 'chun'

import csv


def readcsv():
    twse_id_list = []
    gtsm_id_list = []
    stock_id_dict = {}
    csv_file_list = ['TWSE_price_ranking.csv', 'GTSM_price_ranking.csv']

    for filename in csv_file_list:
        with open(filename, 'rb') as csvfile:
            twsereader = csv.DictReader(csvfile, ['代碼', '名稱', '成交'])
            for row in twsereader:
                if row['代碼'] == '代碼':
                    pass
                else:
                    if filename == csv_file_list[0]:
                        twse_id_list.append(row['代碼'])
                    if filename == csv_file_list[1]:
                        gtsm_id_list.append(row['代碼'])
        csvfile.close()

    stock_id_dict['TWSE_ID_LIST'] = twse_id_list
    stock_id_dict['GTSM_ID_LIST'] = gtsm_id_list
    # print stock_id_dict
    return stock_id_dict

# debug log
# readcsv()