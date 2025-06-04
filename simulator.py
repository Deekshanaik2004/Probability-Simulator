import numpy as np

def simulate_coin_toss(n):
    return np.random.choice(['Heads', 'Tails'], size=n)

def simulate_dice_roll(n):
    return np.random.randint(1, 7, size=n)