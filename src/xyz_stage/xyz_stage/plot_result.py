import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("alignment_history.csv")

# Power
plt.figure(figsize=(8,4))
plt.plot(df["step"], df["power"])
plt.title("Power")
plt.xlabel("Step")
plt.ylabel("Power")
plt.grid(True)
plt.savefig("power.png")

# Gap
plt.figure(figsize=(8,4))
plt.plot(df["step"], df["gap"])
plt.title("Gap")
plt.xlabel("Step")
plt.ylabel("Gap")
plt.grid(True)
plt.savefig("gap.png")

# X
plt.figure(figsize=(8,4))
plt.plot(df["step"], df["x"])
plt.title("X Position")
plt.xlabel("Step")
plt.ylabel("X")
plt.grid(True)
plt.savefig("x_position.png")