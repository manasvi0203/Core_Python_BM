import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("xclara.csv")

print(df)

plt.scatter(df["V1"], df["V2"], color="r")
plt.show()

