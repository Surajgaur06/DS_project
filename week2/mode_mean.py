import pandas as  pd
import numpy as np 

df = pd.DataFrame({ 'Age' : [25, 30, np.nan, 40, 35],
                   'Departement' : ['Hr', 'Finance','Finance', np.nan, 'IT']})
print(df)

df[ 'Age' ] =df['Age'].fillna(df['Age'].mean())

df['Departement']=df['Departement'].fillna(df['Departement'].mode()[0])
print(df)