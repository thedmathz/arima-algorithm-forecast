import sys
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA

# Sample data (replace this with your dynamic input)
data = [1200, 1350, 1600, 2000, 2100, 2500, 3000, 2900, 2400, 1800, 1500, 1300]

model = ARIMA(data, order=(1, 1, 1))
model_fit = model.fit()
forecast = model_fit.forecast(steps=3)

# Output forecast as comma-separated values
print(','.join([str(round(val)) for val in forecast]))
