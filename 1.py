import pandas as pd
import Quandl
df = data = Nasdaqdatalink.get_table("QDL/FON", paginate=True)
print(df.head())
