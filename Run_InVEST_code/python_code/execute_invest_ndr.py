# coding=UTF-8
# -----------------------------------------------
# Generated by InVEST 3.13.0 on Sun May  5 13:34:30 2024
# Model: Nutrient Delivery Ratio

import logging
import sys

import natcap.invest.ndr.ndr
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
    'biophysical_table_path': '/Users/shunkeikakimoto/Files/base_data/mesh/biophysical_table.csv',
    'calc_n': False,
    'calc_p': True,
    'dem_path': '/Users/shunkeikakimoto/Files/base_data/mesh/DEM/slv_elev.tif',
    'k_param': '2',
    'lulc_path': '/Users/shunkeikakimoto/Files/base_data/seals_out_lulc/slv_lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2030_clipped.tif',
    'results_suffix': '',
    'runoff_proxy_path': '/Users/shunkeikakimoto/Files/base_data/mesh/worldclim/ppt_slv.tif',
    'subsurface_critical_length_n': '',
    'subsurface_eff_n': '',
    'threshold_flow_accumulation': '1000',
    'watersheds_path': '/Users/shunkeikakimoto/Files/base_data/mesh/hydrosheds/hydrobasin_slv_lev06.shp',
    'workspace_dir': '/Users/shunkeikakimoto/Files/base_data/slv_InVEST_out/ssp1_rcp26/NutrientRetention/y2030',
}

if __name__ == '__main__':
    natcap.invest.ndr.ndr.execute(args)
