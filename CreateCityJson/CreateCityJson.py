#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')
CSV_FILE_NAME = './CreateCityJson/citys'
JSON_FILE_NAME = './CreateCityJson/citys_json.txt'


orig_df = pd.read_csv(CSV_FILE_NAME)
#拆分，得到城市
city_df = pd.DataFrame(orig_df[u'name'].str.split('\001').tolist(),
                       columns=['province_id', 'province_name', 'province_short_name', 'city_id', 'city_name'])
#只取地级市以上数据，city_id 以00结尾
city_df = city_df[city_df['city_id'].str.endswith('00')]
#去重，得到省份
province_df = city_df.drop_duplicates(subset=['province_id', 'province_name'], keep='first',inplace=False)
province_list = []
for i in range(len(province_df)):
    province = province_df.iloc[i]
    province_name = province['province_name']
    province_short_name = province['province_short_name']
    province_id = province['province_id']
    province_city_df = city_df[city_df['province_id'] == province_id]
    region_list =[]
    for j in range(len(province_city_df)):
        city= province_city_df.iloc[j]
        region_list.append({'order': j, 'code': city['city_id'], 'name': city['city_name']})
    province_list.append({'order': i, 'name': province_name, 'code': province_short_name, 'regions': region_list})

with open(JSON_FILE_NAME, 'wb') as f:
    json.dump(province_list, f, indent=4, encoding='UTF-8', ensure_ascii=False)
print 'Citys json file is ok!'


