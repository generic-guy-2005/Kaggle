import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../Datasets/train.csv")
sns.countplot(x="Pclass", data=df)
plt.savefig("kaggle_figure03.png")