import math
import subprocess
import time

# 最適位置（ウェハ左中央）
tx_x = -1.2
tx_y = 0.0
tx_z = 0.08

# RX開始位置（右側）
rx_x = 1.0
rx_y = 0.3
rx_z = 0.12

step = 0.02

history = []


def power(tx_x, tx_y, tx_z,
          rx_x, rx_y, rx_z):

    dx = tx_x - rx_x
    dy = tx_y - rx_y
    dz = tx_z - rx_z

    return (
        math.exp(-(dx * dx) * 25)
        * math.exp(-(dy * dy) * 25)
        * math.exp(-(dz * dz) * 200)
    )

for i in range(150):

    current = power(
        tx_x, tx_y, tx_z,
        rx_x, rx_y, rx_z
    )

    candidates = [

        (rx_x + step, rx_y, rx_z),
        (rx_x - step, rx_y, rx_z),

        (rx_x, rx_y + step, rx_z),
        (rx_x, rx_y - step, rx_z),

        (rx_x, rx_y, rx_z + step),
        (rx_x, rx_y, rx_z - step)

    ]

    best_power = current
    best_pos = (rx_x, rx_y, rx_z)

    for x, y, z in candidates:

        p = power(
            tx_x, tx_y, tx_z,
            x, y, z
        )

        if p > best_power:
            best_power = p
            best_pos = (x, y, z)

    rx_x, rx_y, rx_z = best_pos

    history.append([
        i,
        rx_x,
        rx_y,
        rx_z,
        best_power
    ])

    subprocess.run(
        [
            "gz", "model",
            "-m", "rx_fiber",
            "-x", str(rx_x),
            "-y", str(rx_y),
            "-z", str(rx_z)
        ]
    )

    print(
        f"{i:03d}",
        f"x={rx_x:.3f}",
        f"y={rx_y:.3f}",
        f"z={rx_z:.3f}",
        f"power={best_power:.6f}"
    )

    time.sleep(0.2)

print("\nXYZ ALIGNMENT COMPLETE")

with open("alignment_history.csv", "w") as f:

    f.write("step,x,y,z,power\n")

    for row in history:

        f.write(
            f"{row[0]},"
            f"{row[1]},"
            f"{row[2]},"
            f"{row[3]},"
            f"{row[4]}\n"
        )

print("alignment_history.csv saved")
