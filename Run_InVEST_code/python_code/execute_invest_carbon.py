# coding=UTF-8
# -----------------------------------------------
# Generated by InVEST 3.13.0 on Sun May  5 10:23:51 2024
# Model: Carbon Storage and Sequestration

import logging
import sys

import natcap.invest.carbon
import natcap.invest.utils

LOGGER = logging.getLogger(__name__)
root_logger = logging.getLogger()

handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter(
    fmt=natcap.invest.utils.LOG_FMT,
    datefmt='%m/%d/%Y %H:%M:%S ')
handler.setFormatter(formatter)
logging.basicConfig(level=logging.INFO, handlers=[handler])

args = {
    'calc_sequestration': False,
    'carbon_pools_path': '/Users/shunkeikakimoto/Files/base_data/mesh/biophysical_table.csv',
    'discount_rate': '',
    'do_redd': False,
    'do_valuation': False,
    'lulc_cur_path': '/Users/shunkeikakimoto/Files/base_data/seals_out_lulc/slv_lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2030_clipped.tif',
    'lulc_cur_year': '',
    'lulc_fut_path': '',
    'lulc_fut_year': '',
    'lulc_redd_path': '',
    'price_per_metric_ton_of_c': '',
    'rate_change': '',
    'results_suffix': '',
    'workspace_dir': '/Users/shunkeikakimoto/Files/base_data/slv_InVEST_out/ssp1_rcp26/CarbonStorage/y2030',
}

if __name__ == '__main__':
    natcap.invest.carbon.execute(args)
