import pandas as pd
from fredapi import Fred
import matplotlib.pyplot as plt

# API key for FRED (replace this with your own API key)
api_key = 'f31656a9c8858f66720eb99c61c196dd'

# connect to FRED API
fred = Fred(api_key=api_key)

# retrieve CPI-U data since 2000
cpi_data = fred.get_series('CPALTT01USM657N')
# cpi_data.head()
# calculate inflation since 2000
inflation = (cpi_data / cpi_data.loc['2000-01-01']) * 100 - 100

# plot inflation data
plt.plot(inflation)
plt.title('Inflation Since 2000 (CPI-U)')
plt.xlabel('Year')
plt.ylabel('Inflation (%)')
plt.show()