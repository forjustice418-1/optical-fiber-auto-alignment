import math
import subprocess
import time

tx_x = 0.0
tx_y = 0.0

rx_x = 0.4
rx_y = 0.2

step = 0.02


def power(tx_x, tx_y, rx_x, rx_y):

    dx = tx_x - rx_x
    dy = tx_y - rx_y

    return math.exp(
        -(dx * dx + dy * dy) * 10
    )


for i in range(50):

    current = power(
        tx_x,
        tx_y,
        rx_x,
        rx_y
    )

    candidates = [

        (rx_x + step, rx_y),
        (rx_x - step, rx_y),

        (rx_x, rx_y + step),
        (rx_x, rx_y - step)

    ]

    best_power = current
    best_x = rx_x
    best_y = rx_y

    for x, y in candidates:

        p = power(
            tx_x,
            tx_y,
            x,
            y
        )

        if p > best_power:

            best_power = p

            best_x = x
            best_y = y

    rx_x = best_x
    rx_y = best_y

    subprocess.run(
        f"gz model "
        f"-m rx_fiber "
        f"-x {rx_x} "
        f"-y {rx_y} "
        f"-z 0.5",
        shell=True
    )

    print(
        f"{i:02d}",
        f"x={rx_x:.3f}",
        f"y={rx_y:.3f}",
        f"power={best_power:.4f}"
    )

    time.sleep(0.5)

print()
print("ALIGNMENT COMPLETE")
