import numpy as np
import matplotlib.pyplot as plt

# Roll a fair six-sided die 1000 times
np.random.seed(42)
rolls = np.random.randint(1, 7, size=1000)

# (a) First 10 rolls
print("First 10 rolls:", rolls[:10])

# (b) Count each face
faces, counts = np.unique(rolls, return_counts=True)

# (c) Empirical vs theoretical probability
theoretical = 1 / 6
print(f"{'Face':<6}{'Count':<8}{'Empirical P':<14}{'Theoretical P'}")
for face, count in zip(faces, counts):
    print(f"{face:<6}{count:<8}{count / 1000:<14.3f}{theoretical:.4f}")

# (d) Histogram saved as die_rolls.png
plt.figure(figsize=(7, 4))
plt.hist(rolls, bins=np.arange(1, 8) - 0.5, color="steelblue", edgecolor="black", rwidth=0.8)
plt.xticks(range(1, 7))
plt.xlabel("Die Face")
plt.ylabel("Frequency")
plt.title("1000 Rolls of a Fair Six-Sided Die")
plt.tight_layout()
plt.savefig("die_rolls.png")
print("Saved die_rolls.png")