import pandas as  pd
import numpy as np 

df = pd.DataFrame({ 'Age' : [25, 30, np.nan, 40, 35],
                   'Departement' : ['Hr', 'Finance','Finance', np.nan, 'IT']
})
print("Original Dataset")
print(df)

df_drop_rows = df.dropna(axis=1)
print("After dropping columns:\n", df_drop_rows)