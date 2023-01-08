"""Script to download HadISST data."""

import requests


sst_request = requests.get('https://www.metoffice.gov.uk/hadobs/hadisst/data/HadISST_sst.nc.gz')
with open('/g/data/ia39/aus-ref-clim-data-nci/hadisst/data/HadISST_sst.nc.gz', 'wb') as sst_file:
    sst_file.write(sst_request.content)

ice_request = requests.get('https://www.metoffice.gov.uk/hadobs/hadisst/data/HadISST_ice.nc.gz')
with open('/g/data/ia39/aus-ref-clim-data-nci/hadisst/data/HadISST_ice.nc.gz', 'wb') as ice_file:
    ice_file.write(ice_request.content)

