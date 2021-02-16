import pandas as pd
import random
import string
data = {
       'bread': list(random.randint(0,1) for i in range(1,50)),
        'sauce': list(random.randint(0,1) for i in range(1,50)),
        'vodka': list(random.randint(0,1) for i in range(1,50)),
        'beer': list(random.randint(0,1) for i in range(1,50))
        
        }

df = pd.DataFrame (data, columns = ['bread','sauce','vodka','beer'],index=list(range(1,50)))
df.index.name = "id"
print (df)
df.to_csv("marketbasket.csv")