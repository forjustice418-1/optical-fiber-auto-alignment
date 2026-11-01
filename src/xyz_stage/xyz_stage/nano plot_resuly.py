import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("alignment_history.csv")

# Power
plt.figure(figsize=(8,4))
plt.plot(df["step"], df["power"])
plt.xlabel("Step")
plt.ylabel("Power")
plt.title("Power vs Step")
plt.grid(True)
plt.savefig("power.png")

# Gap
plt.figure(figsize=(8,4))
plt.plot(df["step"], df["gap"])
plt.xlabel("Step")
plt.ylabel("Gap")
plt.title("Gap vs Step")
plt.grid(True)
plt.savefig("gap.png")

# X position
plt.figure(figsize=(8,4))
plt.plot(df["step"], df["x"])
plt.xlabel("Step")
plt.ylabel("X Position")
plt.title("X Position vs Step")
plt.grid(True)
plt.savefig("x_position.png")

print("Saved:")
print(" power.png")
print(" gap.png")
print(" x_position.png")