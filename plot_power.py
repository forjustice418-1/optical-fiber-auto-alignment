import csv
import matplotlib.pyplot as plt

steps = []
powers = []

with open("alignment_history.csv", newline="") as f:

    reader = csv.DictReader(f)

    for row in reader:

        steps.append(
            int(row["step"])
        )

        powers.append(
            float(row["power"])
        )

plt.figure(figsize=(8,5))

plt.plot(
    steps,
    powers,
    linewidth=2
)

plt.xlabel("Step")
plt.ylabel("Power")
plt.title("Optical Alignment")

plt.grid(True)

plt.savefig(
    "power_graph.png",
    dpi=300
)

plt.show()
