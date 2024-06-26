# coding=UTF-8
# -----------------------------------------------
# Generated by InVEST 3.13.0 on Sun May  5 17:25:38 2024
# Model: Crop Pollination

import logging
import sys

import natcap.invest.pollination
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
    'farm_vector_path': '',
    'guild_table_path': '/Users/shunkeikakimoto/Files/base_data/mesh/guild_table.csv',
    'landcover_biophysical_table_path': '/Users/shunkeikakimoto/Files/base_data/mesh/biophysical_table.csv',
    'landcover_raster_path': '/Users/shunkeikakimoto/Files/base_data/seals_out_lulc/slv_lulc_esa_seals7_ssp1_rcp26_luh2-message_bau_2030_clipped.tif',
    'results_suffix': '',
    'workspace_dir': '/Users/shunkeikakimoto/Files/base_data/slv_InVEST_out/ssp1_rcp26/CropPollination/y2030',
}

if __name__ == '__main__':
    natcap.invest.pollination.execute(args)
