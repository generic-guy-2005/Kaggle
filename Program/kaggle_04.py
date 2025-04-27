import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../Datasets/train.csv")
sns.countplot(x="Sex", hue="Survived", data=df)
plt.title("Survival by Gender")
plt.savefig("kaggle_figure02.png")