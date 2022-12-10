""" 
Consider the following dataset.
Product	Price	Discount
ABC	630	No
DDD	790	Yes
XYZ	250	No
AAA	370	Yes
CCC	880	Yes
PPP	1250	No
NNN	550	No
RRR	700	Yes

"""

# (a) Randomly select a row from the data.

import pandas as pd
import numpy as np

data = {
    "Product": ["ABC", "DDD", "XYZ", "AAA", "CCC", "NNN", "RRR"],
    "Price": [630, 790, 250, 880, 1250, 550, 700],
    "Discount": ["No", "Yes", "No", "Yes", "Yes", "No", "No", "Yes"]
}

df = pd.DataFrame(data)
df.sample()

# (b) Randomly select 3 rows from the data without replacement and analyze it.

op = df.sample(3, replace=False)
op
op.describe()

# (c) Randomly select 2 samples of products with and without discounts each and analyze it.

dt = df.groupby("Discoun").sample(n=3)
dt.describe()
