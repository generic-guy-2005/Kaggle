import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../Datasets/train.csv")
sns.countplot(x="Survived", data=df)
plt.title("Survival Count")
plt.savefig("kaggle_figure01.png")