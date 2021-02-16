import pandas as pd
import random
import string
data = {
        'Name': list(''.join(random.choices(string.ascii_uppercase, k = 5)) for i in range(1,50)),
        'Gender': list(" ".join(random.choices(['M','F',''])) for i in range(1,50)),
        'State': list(''.join(random.choices(['karnataka','kerala','tamilnadu','andhra',''])) for i in range(1,50)),
        'age': list(random.randint(12,60) for i in range(1,50)),
        'experience': list(random.randint(1,15) for i in range(1,50))
        }

df = pd.DataFrame (data, columns = ['Name','Gender','State','age','experience'],index=list(range(1,50)))
df.index.name = "id"
print (df)
df.to_csv("output.csv")