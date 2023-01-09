# HadISST

## Overview

The Met Office Hadley Centre's sea ice and sea surface temperature (SST) data set, HadISST1,
consists of monthly globally-complete fields of SST and sea ice concentration
on a 1 degree latitude-longitude grid from 1870 to date.

More information is available from the [HadISST website](https://www.metoffice.gov.uk/hadobs/hadisst/).

## Data download

We downloaded the HadISST dataset in netCDF format from the
[HadISST download page](https://www.metoffice.gov.uk/hadobs/hadisst/data/download.html)
using a python based code.

The code uses the requests module to download the files. To run it:
```
$ python hadisst.py
```

Monthly updates are managed via the
[Jenkins accessdev server](https://accessdev.nci.org.au/jenkins/job/aus-ref-clim-data-nci/job/HadISST/).

## Data location

We've downloaded HadISST data to:

```
/g/data/ia39/aus-ref-clim-data-nci/hadisst/data/<files>
```

## License

According to the [HadISST terms and conditions](https://www.metoffice.gov.uk/hadobs/hadisst/terms_and_conditions.html),
HadISST is subject to Crown copyright protection and is provided under a Non-Commercial Government Licence.
Further information about the licence can be obtained from
[here](https://www.nationalarchives.gov.uk/doc/non-commercial-government-licence/version/2/). 

## Reference

Rayner NA, Parker DE, Horton EB, Folland CK, Alexander LV, Rowell DP, Kent EC, Kaplan A (2003).
Global analyses of sea surface temperature, sea ice, and night marine air temperature since the late nineteenth century.
*Journal of Geophysical Research*. 108, D14, 4407. https://doi.org/10.1029/2002JD002670

## Acknowledgement

According to the [HadISST terms and conditions](https://www.metoffice.gov.uk/hadobs/hadisst/terms_and_conditions.html),
users should include one of the following:
- For use in the UK, “HadISST data were obtained from https://www.metoffice.gov.uk/hadobs/hadisst/ and are Crown Copyright, Met Office, [year of first publication], provided under a Non-Commercial Government Licence http://www.nationalarchives.gov.uk/doc/non-commercial-government-licence/version/2/”.
- For use outside the UK, “HadISST data were obtained from https://www.metoffice.gov.uk/hadobs/hadisst/ and are British Crown Copyright, Met Office, [year of first publication], provided under a Non-Commercial Government Licence http://www.nationalarchives.gov.uk/doc/non-commercial-government-licence/version/2/”.

The source should also be quoted in the acknowledgements section as www.metoffice.gov.uk/hadobs. 

## Assistance

For assistance with HadISST data on NCI, open a new issue at https://github.com/aus-ref-clim-data-nci/HadISST/issues

