import pandas as pd
from serial import Serial

dat = pd.read_csv("pokemon.csv",skiprows = [1,2,3])
pas = []
def rem():
    pas.append(dat[dat["Pokemon"] == "Dusknoir"])
    print(pas)

