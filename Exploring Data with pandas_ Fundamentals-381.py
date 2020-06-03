## 1. Introduction to the Data ##

f500_head=f500.head(10)
f500.info()

## 2. Vectorized Operations ##

rank_change=f500["previous_rank"]-f500["rank"]

## 3. Series Data Exploration Methods ##

rank_change =  f500["previous_rank"] - f500["rank"]
rank_change_max=rank_change.max()
rank_change_min=rank_change.min()


## 4. Series Describe Method ##

rank=f500["rank"]
rank_desc=rank.describe()
prev_rank=f500["previous_rank"]
prev_rank_desc=prev_rank.describe()

## 5. Method Chaining ##

previous_rank=f500["previous_rank"]
previous_rank_count=previous_rank.value_counts()
zero_previous_rank=previous_rank_count.loc[0]
zero_previous_rank=f500["previous_rank"].value_counts().loc[0]

## 6. Dataframe Exploration Methods ##

max_f500=f500.max(numeric_only=True)

## 7. Dataframe Describe Method ##

import numpy as np
f500_desc=f500.describe(include=[np.number])

## 8. Assignment with pandas ##

ceo_dow_chemical=f500.loc["Dow Chemical","ceo"]
ceo_dow_chemical="Jim Fitterling"
f500.loc["Dow Chemical","ceo"]="Jim Fitterling"

## 9. Using Boolean Indexing with pandas Objects ##

motor_bool=f500["industry"]=="Motor Vehicles and Parts"
motor_countries=f500.loc[motor_bool,"country"]

## 10. Using Boolean Arrays to Assign Values ##

import numpy as np
prev_rank_before = f500["previous_rank"].value_counts(dropna=False).head()
previous_rank_bool=f500["previous_rank"]==0
f500.loc[previous_rank_bool,"previous_rank"]=np.nan
prev_rank_after=f500["previous_rank"].value_counts(dropna=False).head()

## 11. Creating New Columns ##

f500["rank_change"]=f500["previous_rank"]-f500["rank"]
rank_change_desc=f500["rank_change"].describe()     

## 12. Challenge: Top Performers by Country ##

industry_bool=f500["country"]=="USA"
industry_usa=f500.loc[industry_bool,"industry"]
industry_usa=industry_usa.value_counts().head(2)
sector_bool=f500["country"]=="China"
sector_china=f500.loc[sector_bool,"sector"].value_counts().head(3)

## 12. Challenge: Top Performers by Country ##

industry_bool=f500["country"]=="USA"
industry_usa=f500.loc[industry_bool,"industry"]
industry_usa=industry_usa.value_counts().head(2)
sector_bool=f500["country"]=="China"
sector_china=f500.loc[sector_bool,"sector"].value_counts().head(3)