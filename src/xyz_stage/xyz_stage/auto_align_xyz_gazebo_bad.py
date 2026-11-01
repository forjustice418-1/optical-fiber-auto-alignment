import math
import subprocess
import time
import random

# 最適位置（ウェハ左中央）
tx_x = -1.2
tx_y = 0.0
tx_z = 0.08

# RX開始位置（右側）
rx_x = 1.0
rx_y = 0.3
rx_z = 0.12

step = 0.02

safe_gap = 0.03

position_error = 0.005

crosstalk = 0.15

history = []


def actual_position(x, y, z):

    actual_x = (
        x
        + random.uniform(
            -position_error,
            position_error
        )
    )

    actual_y = (
        y
        + random.uniform(
            -position_error,
            position_error
        )
    )

    actual_z = (
        z
        + random.uniform(
            -position_error,
            position_error
        )
    )

    return (
        actual_x,
        actual_y,
        actual_z
    )


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

    ax, ay, az = actual_position(
    rx_x,
    rx_y,
    rx_z
)

current = power(
    tx_x,
    tx_y,
    tx_z,
    ax,
    ay,
    az
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

        ax, ay, az = actual_position(
    x,
    y,
    z
)

p = power(
    tx_x,
    tx_y,
    tx_z,
    ax,
    ay,
    az
)

        if p > best_power:
            best_power = p
            best_pos = (x, y, z)

    rx_x, rx_y, rx_z = best_pos

    rx_y += random.uniform(
    -crosstalk,
    crosstalk
) * 0.01

rx_z += random.uniform(
    -crosstalk,
    crosstalk
) * 0.01


    if rx_x < (tx_x + safe_gap):

    rx_x = tx_x + safe_gap


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
