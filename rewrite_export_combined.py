#!/usr/bin/env python3

import csv
import json
import sys
from functools import reduce
from os import path

input_file = sys.argv[1]
(base, ext) = path.splitext(input_file)
assert ext == '.json', "Expected json file but extension is {}".format(ext)

output_file = "{}.csv".format(base)

replace_keys = {
    'geom': 'WKT',
    'district_geom': 'WKT',
    'dl_ip_count': 'dl_count_ips',
    'ul_ip_count': 'ul_count_ips',
    'dl_test_count': 'dl_count_tests',
    'ul_test_count': 'ul_count_tests',
    'dl_Mbps': 'download_Mbps',
    'ul_Mbps': 'upload_Mbps',
    'dl_min_rtt': 'min_rtt',
    'legal_area_name': 'name',
    'county_name': 'name',
    'slice':'fcc',
    'dl':'ml_dl',
    'ul':'ml_ul',
    'provider_count': 'reg_provider_count',
}

def rewrite_row(json_row):
    "Flattens a json row into a dict with scalar values"
    row = dict()
    for k, v in json_row.items():
        if k in ('dl', 'ul', 'slice'):
            for time_slice in v:
                time_period = time_slice.get('time_period')
                if not time_period:
                    continue
                for k2, v2 in time_slice.items():
                    if k2 != 'time_period':
                        name = k2
                        name = replace_keys.get(name,name)
                        row["{}_{}_{}".format(replace_keys.get(k,k), name, time_period)] = v2
        else:
            k = replace_keys.get(k, k)
            row[k] = v
    return row

with open(input_file) as results_file:
    results = [json.loads(line) for line in results_file.readlines()]

fields = reduce(lambda a, b: a | b, (set(rewrite_row(r)) for r in results))
fields = list(fields)
if 'WKT' in fields:
    fields.remove('WKT') # remove, then append to ensure WKT is last column.
    fields.sort()
    fields.append('WKT')

# copied from the working county layer
expected_fields = ['ml_dl_count_tests_dec_2014', 'ml_dl_count_tests_jun_2015', 'ml_dl_count_tests_dec_2015', 'ml_dl_count_tests_jun_2016', 'ml_dl_count_tests_dec_2016', 'ml_dl_count_tests_jun_2017', 'ml_dl_count_tests_dec_2017', 'ml_dl_count_tests_jun_2018', 'ml_dl_count_tests_dec_2018', 'ml_upload_Mbps_dec_2014', 'ml_upload_Mbps_jun_2015', 'ml_upload_Mbps_dec_2015', 'ml_upload_Mbps_jun_2016', 'geoid', 'ml_upload_Mbps_dec_2016', 'ml_upload_Mbps_jun_2017', 'ml_ul_count_ips_dec_2014', 'ml_ul_count_ips_jun_2015', 'ml_upload_Mbps_dec_2017', 'ml_upload_Mbps_jun_2018', 'ml_ul_count_ips_dec_2015', 'ml_ul_count_ips_jun_2016', 'ml_upload_Mbps_dec_2018', 'ml_ul_count_ips_dec_2016', 'ml_ul_count_ips_jun_2017', 'ml_ul_count_ips_dec_2017', 'ml_ul_count_ips_jun_2018', 'ml_ul_count_ips_dec_2018', 'ml_download_Mbps_dec_2014', 'ml_download_Mbps_jun_2015', 'ml_download_Mbps_dec_2015', 'ml_download_Mbps_jun_2016', 'ml_download_Mbps_dec_2016', 'ml_download_Mbps_jun_2017', 'ml_download_Mbps_dec_2017', 'ml_download_Mbps_jun_2018', 'ml_download_Mbps_dec_2018', 'fcc_advertised_down_dec_2014', 'fcc_advertised_down_jun_2015', 'fcc_advertised_down_dec_2015', 'fcc_advertised_down_jun_2016', 'fcc_advertised_down_dec_2016', 'fcc_advertised_down_jun_2017', 'ml_ul_count_tests_dec_2014', 'ml_ul_count_tests_jun_2015', 'fcc_advertised_down_dec_2017', 'ml_ul_count_tests_dec_2015', 'ml_ul_count_tests_jun_2016', 'ml_ul_count_tests_dec_2016', 'ml_ul_count_tests_jun_2017', 'ml_ul_count_tests_dec_2017', 'ml_ul_count_tests_jun_2018', 'fcc_reg_provider_count_dec_2014', 'fcc_reg_provider_count_jun_2015', 'ml_dl_count_ips_dec_2014', 'ml_dl_count_ips_jun_2015', 'ml_min_rtt_dec_2014', 'ml_min_rtt_jun_2015', 'ml_ul_count_tests_dec_2018', 'fcc_reg_provider_count_dec_2015', 'fcc_reg_provider_count_jun_2016', 'fcc_advertised_up_dec_2014', 'fcc_advertised_up_jun_2015', 'ml_dl_count_ips_dec_2015', 'ml_dl_count_ips_jun_2016', 'ml_min_rtt_dec_2015', 'ml_min_rtt_jun_2016', 'fcc_reg_provider_count_dec_2016', 'fcc_reg_provider_count_jun_2017', 'fcc_advertised_up_dec_2015', 'fcc_advertised_up_jun_2016', 'ml_dl_count_ips_dec_2016', 'ml_dl_count_ips_jun_2017', 'ml_min_rtt_dec_2016', 'ml_min_rtt_jun_2017', 'fcc_reg_provider_count_dec_2017', 'fcc_advertised_up_dec_2016', 'fcc_advertised_up_jun_2017', 'ml_dl_count_ips_dec_2017', 'ml_dl_count_ips_jun_2018', 'ml_min_rtt_dec_2017', 'ml_min_rtt_jun_2018', 'fcc_advertised_up_dec_2017', 'ml_dl_count_ips_dec_2018', 'ml_min_rtt_dec_2018']
#assert 0 == len(set(expected_fields) - set(fields)), \
#    f"Required fields missing: {set(expected_fields) - set(fields)}"

with open(output_file, 'w') as output:
    writer = csv.DictWriter(output, fields)
    writer.writeheader()
    writer.writerows(rewrite_row(r) for r in results)

print(fields)