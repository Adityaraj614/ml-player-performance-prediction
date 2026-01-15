import numpy as np
import pandas as pd
np.random.seed(42)
#np.random.seed(42) fixes the starting point of the pseudo-random number generator,
#ensuring that all randomly generated values are reproducible across runs and machines. 
#This guarantees that the dataset, data splits, and experiments remain consistent, 
#allowing fair model comparison and reliable debugging.
n_samples = 1000

#create inputs for data labels
accuracy = np.random.uniform(40, 100, n_samples)
time_played = np.random.uniform(10,120, n_samples)
deaths =np.random.randint(0,20, n_samples)

# Derive score using gameplay logic
score = (
    accuracy * 10 +
    time_played * 2 -
    deaths * 15 +
    np.random.normal(0, 50, n_samples)
)

# Create performance labels based on score percentiles
low_threshold = np.percentile(score, 33)
high_threshold = np.percentile(score, 66)

performance = []

for s in score:
    if s < low_threshold:
        performance.append(0)      # Poor
    elif s < high_threshold:
        performance.append(1)      # Average
    else:
        performance.append(2)      # Good

df = pd.DataFrame({
    "accuracy": accuracy,
    "time_played": time_played,
    "deaths": deaths,
    "score": score,
    "performance": performance
})

output_path="data/synthetic/player_performance.csv"
df.to_csv(output_path, index= False)
print(f"Synthetic dataset saved at: {output_path}")