import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_coin_toss(results):
    df = pd.DataFrame(results, columns=["Outcome"])
    sns.countplot(x="Outcome", data=df)
    plt.title("Coin Toss Outcomes")
    plt.show()

def plot_dice_roll(results):
    df = pd.DataFrame(results, columns=["Outcome"])
    sns.countplot(x="Outcome", data=df)
    plt.title("Dice Roll Outcomes")
    plt.show()