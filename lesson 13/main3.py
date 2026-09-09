import pandas as pd


data ={'name':["Resa","Donjeta","Aniku"],
        'age':[18,55,58],
       'City':["Viti","Malisheves","Deqanit"]
       }


df = pd.DataFrame(data)

print(df)


fajlli = pd.read_csv("donjeta.csv")

print(fajlli)


teDhenat =fajlli.to_csv("donjeta.csv",index=False)
print(teDhenat)
