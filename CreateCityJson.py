#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import json
CSV_FILE_NAME = 'citys'
JSON_FILE_NAME = 'citys_json.txt'

city_list = pd.read_csv(CSV_FILE_NAME)
#拆分，得到城市
city_df = pd.DataFrame(city_list[u'name'].str.split('\001').tolist(),
                       columns=['province_id', 'province_name', 'province_short_name', 'city_id', 'city_name'])

#去重，得到省份
province_df = city_df.drop_duplicates(subset=['province_id', 'province_name'], keep='first',inplace=False)

for i in range(len(province_df)):
    row = province_df.iloc[i]
    province_name = row['province_name']
    province_id = row['province_id']
    print '%s %s' % (province_id, province_name)
    print json.dumps(['order:',i ,'name:', province_name, 'code:', province_id])
    province_city_df = city_df[city_df['province_id'] == province_id]
    for j in range(len(province_city_df)):
        city_row = province_city_df.iloc[j]
        city_id = city_row['city_id']
        city_name = city_row['city_name']
        print '%s, %s' % (city_id, city_name)


