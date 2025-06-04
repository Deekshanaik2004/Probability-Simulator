from simulator import simulate_coin_toss, simulate_dice_roll
from visualizer import plot_coin_toss, plot_dice_roll
from ml_model import train_model

# Simulate and visualize
coin_results = simulate_coin_toss(1000)
plot_coin_toss(coin_results)

dice_results = simulate_dice_roll(1000)
plot_dice_roll(dice_results)

# Train ML model
model, acc = train_model()
print(f"Trained ML model accuracy on dice prediction: {acc:.2f}")
