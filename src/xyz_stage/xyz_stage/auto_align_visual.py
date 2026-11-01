import math
import subprocess
import time

tx_x = 0.0
rx_x = 0.8

step = 0.05


def power(tx, rx):
    dx = tx - rx
    return math.exp(-(dx ** 2) * 5)


for i in range(20):

    current = power(tx_x, rx_x)

    left = power(tx_x, rx_x - step)
    right = power(tx_x, rx_x + step)

    if left > current:
        rx_x -= step

    elif right > current:
        rx_x += step

    print(
        f"STEP {i:02d}",
        f"RX={rx_x:.3f}",
        f"POWER={power(tx_x, rx_x):.4f}"
    )

    subprocess.run(
        f"gz model -m xyz_stage -x {rx_x} -y 0 -z 0.1",
        shell=True
    )

    time.sleep(0.5)
